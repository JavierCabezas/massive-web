from django.db import models
from ..users.models import User
from ..music_packs.models import MusicPack
from ..music_tracks.models import MusicTrack


class Cart(models.Model):
    creation_date = models.DateTimeField(
        null=False
    )

    payment_date = models.DateTimeField(
        null=True
    )

    deleted_date = models.DateTimeField(
        null=True
    )

    amount = models.FloatField(
        null=False
    )

    user = models.ForeignKey(User)

    music_packs = models.ManyToManyField(MusicPack)

    music_tracks = models.ManyToManyField(MusicTrack)
