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

    category = models.ForeignKey(Category, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    music_packs = models.ManyToManyField(MusicPack, blank=True)

    music_tracks = models.ManyToManyField(MusicTrack, blank=True)

    def __str__(self):
        return self.name

    def backend(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_es': self.name_es,
            'intro': self.intro,
            'intro_es': self.intro_es,
            'post': self.post,
            'post_es': self.post_es,
            'image': settings.BASE_URL + self.image.name,
            'tags': [tag.backend() for tag in self.tags.all()]
        }
