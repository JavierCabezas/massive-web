# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('surname', models.TextField(max_length=200, null=True)),
                ('status', models.IntegerField(default=10, null=True)),
                ('image_url', models.TextField(max_length=300, null=True)),
                ('email', models.TextField(max_length=150, unique=True)),
                ('google_token', models.TextField(null=True)),
                ('google_id', models.TextField(max_length=100, null=True)),
                ('facebook_token', models.TextField(null=True)),
                ('facebook_id', models.TextField(null=True)),
                ('token', models.TextField(max_length=400, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
