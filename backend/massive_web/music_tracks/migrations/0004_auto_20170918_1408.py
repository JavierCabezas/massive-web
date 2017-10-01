# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_tracks', '0003_musictrack_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='musictrack',
            name='long_description_es',
            field=models.TextField(default='_', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musictrack',
            name='short_description_es',
            field=models.TextField(default='_', max_length=160),
            preserve_default=False,
        ),
    ]