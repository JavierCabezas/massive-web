# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20170912_2354'),
        ('authors', '0005_auto_20170917_0046'),
        ('tags', '0002_remove_tag_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('short_description', models.TextField(max_length=160)),
                ('long_description', models.TextField(max_length=2000)),
                ('duration', models.TimeField()),
                ('image', models.ImageField(null=True, upload_to='music_tracks')),
                ('song_preview', models.FileField(null=True, upload_to='music_tracks')),
                ('song', models.FileField(null=True, upload_to='private_music_tracks')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authors.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
        ),
    ]