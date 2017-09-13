from django.db import models


class Tag(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    level = models.IntegerField()

    def __str__(self):
        return self.name
