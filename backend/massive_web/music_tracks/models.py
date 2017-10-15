from django.db import models
from django.conf import settings

from ..authors.models import Author
from ..categories.models import Category
from ..tags.models import Tag


class MusicTrack(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    name_es = models.TextField(
        max_length=200,
        null=False
    )

    author = models.ForeignKey(Author)

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

    price = models.FloatField(
        null=False,
        default=1
    )

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def backend(self, full=False):
        base = {
            'id': self.id,
            'name': self.name,
            'name_es': self.name_es,
            'short_description': self.short_description,
            'short_description_es': self.short_description_es,
            'image': settings.BASE_URL + self.image.name,
            'price': self.price,
            'file': settings.BASE_URL + self.song_preview.name
        }
        if full:
            base['author_id'] = self.author_id
            base['long_description'] = self.long_description
            base['long_description_es'] = self.long_description_es
            base['preview'] = self.song_preview
            base['length'] = self.duration
            base['file'] = settings.BASE_URL + self.song_preview.name

        return base