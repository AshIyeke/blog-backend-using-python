from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Post model with a custom manager to retrieve published posts only
class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


# Blog Post model
class Post(models.Model):
    
    tags = TaggableManager()
    
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    objects = models.Manager()  # The default manager.
    published = PublishManager()  # Our custom manager.

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    # Method to get the absolute URL of a post
    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.strftime("%m"),
                self.publish.strftime("%d"),
                self.slug,
            ],
        )

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            slug = slugify(self.title)
            # Ensure slug is unique for the publication date
            unique_slug = slug
            num = 1
            while Post.objects.filter(
                publish__date=self.publish.date(), slug=unique_slug
            ).exists():
                unique_slug = "{}-{}".format(slug, num)
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Comment by {} on {}".format(self.name, self.post)
