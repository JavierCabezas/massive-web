# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20170912_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image_url',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
