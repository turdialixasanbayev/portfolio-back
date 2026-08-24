from rest_framework import serializers

from apps.post.models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "description",
            "image",
            "published_date",
            "read_time_minutes",
        ]
