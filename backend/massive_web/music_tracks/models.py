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
        on_delete=models.CASCADE
    )

    short_description = models.TextField(
        max_length=160,
        null=False
    )

    long_description = models.TextField(
        max_length=2000,
        null=False
    )

    duration = models.TimeField(
        null=False
    )

    image = models.ImageField(
        upload_to='music_tracks',
        null=True,
    )

    song_preview = models.FileField(
        upload_to='music_tracks',
        null=True,
    )

    song = models.FileField(
        upload_to='private_music_tracks',
        null=True,
    )

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name