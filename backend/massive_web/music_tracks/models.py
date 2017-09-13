from django.db import models

from ..authors.models import Author
from ..categories.models import Category
from ..tags.models import Tag


class MusicTrack(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    short_description = models.TextField(
        max_length=120,
        null=False
    )

    long_description = models.TextField(
        max_length=300,
        null=False
    )

    duration = models.TimeField(
        null=False
    )

    image_url = models.TextField(
        max_length=300,
        null=True
    )

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name