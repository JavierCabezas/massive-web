from django.db import models


class Email(models.Model):
    address = models.TextField(max_length=200, null=False, unique=True)