from django.urls import path

from .api.ProjectList.views import ProjectListView
from .api.PostList.views import PostListView
from .api.PostDetail.views import PostDetailView


urlpatterns = [
    path(
        "projects/",
        ProjectListView.as_view(),
        name="project-list",
    ),
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list",
    ),
    path(
        "posts/<slug:post_slug>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),
]
