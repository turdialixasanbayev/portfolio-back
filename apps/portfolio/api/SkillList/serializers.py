from rest_framework import serializers

from apps.portfolio.models import Skill


class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "title",
        ]
