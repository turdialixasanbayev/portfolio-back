from django.contrib import admin

from .models import (
    Skill, 
    Experience,
)


class SkillAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    search_help_text = "Search a Skills with title."
    list_display = (
        'id',
        'title',
    )


class ExperienceAdmin(admin.ModelAdmin):
    search_help_text = 'Search a Experience with role or company.'
    list_display = (
        'id',
        'role',
        'company',
        'period',
    )
    list_filter = (
        'role',
        'company',
    )
    search_fields = (
        'role',
        'company',
    )


admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
