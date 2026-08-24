from rest_framework import generics

from apps.portfolio.models import Experience
from .serializers import ExperienceListSerializer


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceListSerializer
    pagination_class = None
