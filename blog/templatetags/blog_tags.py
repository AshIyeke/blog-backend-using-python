from django import template
from ..models import Post
from django.db.models import Count

# Register the template library
register = template.Library()


# Simple tag to get the total number of published posts
@register.simple_tag
def total_posts():
    return Post.published.count()


# Inclusion tag to show the latest posts
@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.all()[:count]
    return {"latest_posts": latest_posts}


# Simple tag to get the most commented posts, can be used for assignment
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]
