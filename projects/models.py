from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField
from taggit.managers import TaggableManager

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField()
    slug = models.SlugField(max_length=50)
    featured = models.BooleanField(default=False)
    tags = TaggableManager()
    live_site = models.URLField(max_length=500, blank=True)
    git_repo = models.URLField(max_length=500, blank=True)
    project_detail = models.TextField(blank=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return self.title