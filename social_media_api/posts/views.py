from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            return Response({"detail": "Not allowed."}, status=403)
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"detail": "Not allowed."}, status=403)
        post.delete()
        return Response({"detail": "Post deleted successfully"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            return Response({"detail": "Not allowed."}, status=403)
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({"detail": "Not allowed."}, status=403)
        comment.delete()
        return Response({"detail": "Comment deleted successfully"})


#                     LIKE / UNLIKE VIEWS

class LikePostView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        """Like a post if not already liked."""
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Prevent double liking
        if Like.objects.filter(post=post, user=user).exists():
            return Response({"detail": "You already liked this post"}, status=400)

        # Create like
        Like.objects.create(post=post, user=user)

        # Create notification to post author
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked"})


class UnlikePostView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        """Remove a like if it exists."""
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({"detail": "You have not liked this post"}, status=400)

        like.delete()
        return Response({"detail": "Post unliked"})

#                     FEED VIEW

class FeedView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()

        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)
