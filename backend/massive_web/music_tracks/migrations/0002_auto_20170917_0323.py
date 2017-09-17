# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musictrack',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author'),
        ),
    ]
