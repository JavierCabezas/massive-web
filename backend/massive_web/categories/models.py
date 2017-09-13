from django.db import models


class Category(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    parent_category = models.ForeignKey(
        'self',
        blank=True,
        null=True
    )

    level = models.IntegerField()

    def __str__(self):
        if self.parent_category is None:
            return self.name
        else:
            return '{} - {}'.format(
                self.parent_category.name,
                self.name,
            )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = (
            'parent_category__name',
            'name',
        )