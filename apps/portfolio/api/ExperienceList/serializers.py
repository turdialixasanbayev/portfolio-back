from rest_framework import serializers

from apps.portfolio.models import Experience


class ExperienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "role",
            "company",
            "period",
            "description",
        ]
