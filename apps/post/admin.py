from django.contrib import admin

from .models import (
    Project,
    Post,
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)
    search_fields = ('title',)
    search_help_text = "Search a Post with title."
    date_hierarchy = 'published_date'
    prepopulated_fields = {"slug": ('title',),}
    list_display = (
        'id',
        'title',
        'image',
        'published_date',
        'is_published',
        'read_time_minutes',
    )
    list_filter = (
        'published_date',
        'is_published',
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    search_help_text = "Search a Post with title."
    list_display = (
        'id',
        'title',
        'image',
        'external_url',
    )
