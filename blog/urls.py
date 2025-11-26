from django.urls import path, re_path
from . import views

# Define the application namespace so `include('blog.urls', namespace='blog')`
# is allowed. See django.urls.include() documentation — include() itself does not
# accept an `app_name` keyword.
app_name = "blog"
urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    re_path(
        r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/"
        r"(?P<post>[-\w]+)/$",
        views.post_detail,
        name="post_detail",
    ),
]
