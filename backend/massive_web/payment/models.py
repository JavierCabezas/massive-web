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


    def calculate_amount(self, music_packs, music_tracks):
        """
        Returns the value to pay for an specific cart given the objects of music packs and music tracks given by argument
        These objects are instances of their respective classes
        :param music_packs:
        :param music_tracks:
        :return:
        """
        total = 0
        for mp in music_packs:
            total += mp.price
        for mt in music_tracks:
            total += mt.price
        self.amount = total