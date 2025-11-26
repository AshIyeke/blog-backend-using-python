from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


# Create your views here.


class PostListView(ListView):
    """
    Class-based view to list published posts with pagination.
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


# View function for single post detail
def post_detail(request, year, month, day, post):
    """Display a single post (published) identified by slug & publish date."""

    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, "blog/post/detail.html", {"post": post})
