# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_remove_tag_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name_es',
            field=models.TextField(default='_', max_length=200),
            preserve_default=False,
        ),
    ]
