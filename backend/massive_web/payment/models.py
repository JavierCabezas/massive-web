from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

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

    def paypal_request(self):
        paypal_dict = {
            "business": "receiver_email@example.com",
            "amount": "10000000.00",
            "item_name": "name of the item",
            "invoice": "unique-invoice-id",
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": request.build_absolute_uri(reverse('your-return-view')),
            "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
            "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
        }