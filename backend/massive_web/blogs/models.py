from django.db import models
from django.conf import settings

from ..categories.models import Category
from ..tags.models import Tag
from ..authors.models import Author
from ..music_tracks.models import MusicTrack
from ..music_packs.models import MusicPack

class Blog(models.Model):
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

    intro = models.TextField(
        max_length=2000,
        null=False
    )

    intro_es = models.TextField(
        max_length=160,
        null=False
    )

    post = models.TextField(
        null=False
    )

    post_es = models.TextField(
        null=False
    )

    image = models.ImageField(
        upload_to='blog',
    )

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag)

    music_packs = models.ManyToManyField(MusicPack)

    music_tracks = models.ManyToManyField(MusicTrack)

    def __str__(self):
        return self.name

    def backend(self):
        return {
            'id': self.id,
            'intro': self.intro,
            'intro_es': self.intro_es,
            'post': self.post,
            'post_es': self.post_es,
            'image': settings.BASE_URL + self.image.name
        }