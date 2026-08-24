from django.utils import timezone

from rest_framework import generics

from apps.post.models import Post
from .serializers import PostListSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(
        is_published=True,
        published_date__lte=timezone.localdate(),
    )
    serializer_class = PostListSerializer
