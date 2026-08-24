from rest_framework import serializers

from apps.post.models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "image",
            "external_url",
        ]
