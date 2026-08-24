from django.urls import path

from .api.SkillList.views import SkillListView
from .api.ExperienceList.views import ExperienceListView


urlpatterns = [
    path(
        "skills/",
        SkillListView.as_view(),
        name="skill-list",
    ),
    path(
        "experiences/",
        ExperienceListView.as_view(),
        name="experience-list",
    ),
]
