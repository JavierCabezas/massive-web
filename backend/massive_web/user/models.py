from django.db import models

class User(models.Model):
    name = models.TextField(max_length=200, null=False)
    surname = models.TextField(max_length=200, null=True)
    status = models.IntegerField(null=True, default=10)
    image_url = models.TextField(max_length=300, null=True)
    email = models.TextField(max_length=150, unique=True, null=False)
    google_token = models.TextField(null=True)
    google_id = models.TextField(max_length=100, null=True)
    facebook_token = models.TextField(null=True)
    facebook_id = models.TextField(null=True)
    token = models.TextField(max_length=500, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)