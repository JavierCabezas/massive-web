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

    def backend_detail(self):
        similar_packs = MusicPack.objects.filter(category_id__in=self.category.family()).exclude(id=self.id)
        return {
            'id': self.id,
            'img' : settings.BASE_URL + self.image.name,
            'title': self.name,
            'title_es': self.name_es,
            'price': self.price,
            'short_description': self.short_description,
            'short_description_es': self.short_description_es,
            'long_description': self.long_description,
            'long_description_es': self.long_description_es,
            'tracks': [song.backend() for song in self.music_tracks.all()],
            'category': self.category.name,
            'category_es': self.category.name_es,
            'similar': [s.backend() for s in similar_packs]
        }

    @staticmethod
    def id_dict():
        """
        Returns a dictionary with all the objects of this class instance
        :return: Dictionary in the format { id: MusicPack instance model , id:MusicPack instance 2... }
        """
        out = {}
        for mp in MusicPack.objects.all():
            out[mp.id] = mp
        return out

