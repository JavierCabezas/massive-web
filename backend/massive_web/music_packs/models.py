from django.db import models

from ..categories.models import Category
from ..tags.models import Tag
from ..music_tracks.models import MusicTrack
from django.conf import settings

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

    def backend(self):
        return {
            'id': self.id,
            'img': settings.BASE_URL + self.image.name,
            'title': self.name,
            'title_es': self.name_es,
            'text': self.short_description,
            'text_es': self.short_description_es,
            'price': self.price
        }