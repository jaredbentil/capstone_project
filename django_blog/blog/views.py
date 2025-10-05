from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .models import Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from taggit.models import Tag

# This view is handled by the `django_blog/urls.py` for the root URL
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content', 'tags'] # Add 'tags' to fields
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'tags'] # Add 'tags'
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'tags'] # Add 'tags'
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/' # Redirect to home page after deletion

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Note: The 'register' and 'profile' views from the previous task should remain here.
# Make sure to import the necessary forms and decorators for them as well.
# ... (your existing register and profile views)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

def register(request):
    # ... (existing code)
    pass

@login_required
def profile(request):
    # ... (existing code)
    pass

# New view for adding comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        # Find the post this comment belongs to from the URL
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        # Redirect back to the post the comment was on
        post = self.get_object().post
        return reverse_lazy('post-detail', kwargs={'pk': post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Get the tag from the URL slug
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return Post.objects.filter(tags__in=[tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the tag name to the template
        context['tag_name'] = self.kwargs.get('slug')
        return context

class PostSearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Search in title, content, and tags
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context