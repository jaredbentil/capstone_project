# Django & DRF Imports
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Local App Imports
from .models import Post, Comment, Like  # Added 'Like' here
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        # This line will now work because 'Like' is imported
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)
        
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        try:
            # This line will now work because 'Like' is imported
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist: # This will also work now
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)
    

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset provides CRUD actions for Comments.
    The queryset is filtered to only return comments for a specific post.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('post_pk')
        
        post = generics.get_object_or_404(Post, pk=pk)
        
        comment = serializer.save(author=self.request.user, post=post)
        
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb='commented on your post',
                target=comment.post
            )

class FeedView(generics.ListAPIView):
    """
    This view returns a personalized feed of posts from users that the
    current user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')