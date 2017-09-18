from django.db import models

from ..categories.models import Category
from ..tags.models import Tag
from ..music_tracks.models import MusicTrack

class MusicPack(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    name_es = models.TextField(
        max_length=200,
        null=False
    )

    short_description = models.TextField(
        max_length=160,
        null=False
    )

    long_description = models.TextField(
        max_length=2000,
        null=False
    )


    short_description_es = models.TextField(
        max_length=160,
        null=False
    )

    long_description_es = models.TextField(
        max_length=2000,
        null=False
    )

    image = models.ImageField(
        upload_to='music_packs',
        null=True,
    )

    price = models.FloatField(
        null=False,
        default=1
    )

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag)

    music_tracks = models.ManyToManyField(MusicTrack)

    def __str__(self):
        return self.name