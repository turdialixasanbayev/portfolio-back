from rest_framework import generics

from apps.portfolio.models import Skill
from .serializers import SkillListSerializer


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillListSerializer
    pagination_class = None
