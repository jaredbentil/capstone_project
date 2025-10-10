from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # search_fields is used for the SearchFilter backend we'll set up
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        # Automatically set the author to the currently logged-in user
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset provides CRUD actions for Comments.
    The queryset is filtered to only return comments for a specific post.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filter comments based on the post_pk from the URL
        post_pk = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_pk)

    def perform_create(self, serializer):
        # Automatically set the author and the related post
        post_pk = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_pk)
        serializer.save(author=self.request.user, post=post)