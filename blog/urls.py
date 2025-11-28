from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    # View posts by tag
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    # View posts by year, month, day, and slug
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    # View to share a post via email
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    # The comment URL is no longer needed as it's handled in post_detail
    # RSS feed
    path("feed/", LatestPostsFeed(), name="post_feed"),
]
