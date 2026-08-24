from rest_framework import generics

from apps.post.models import Project
from .serializers import ProjectListSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    pagination_class = None
