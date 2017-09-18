from django.db import models


class Tag(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    name_es = models.TextField(
        max_length=200,
        null=False
    )

    def __str__(self):
        return self.name

    def backend(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_es': self.name_es
        }
