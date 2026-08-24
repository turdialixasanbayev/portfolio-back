from django.http import Http404
from django.utils import timezone

from rest_framework import generics

from rest_framework.exceptions import NotFound

from apps.post.models import Post
from .serializers import PostDetailSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(
        is_published=True,
        published_date__lte=timezone.localdate(),
    )
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "post_slug"

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound("Not found.")
