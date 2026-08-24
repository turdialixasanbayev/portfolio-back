from rest_framework import serializers

from apps.post.models import Post


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "description",
            "image",
            "published_date",
            "read_time_minutes",
            "content_html",
        ]
