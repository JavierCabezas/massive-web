from django.db import models


class Category(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    name_es = models.TextField(
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

    def backend(self):
        return {
            'id': self.id,
            'name_en': self.name,
            'name_es': self.name_es,
            'parent_category_id': self.parent_category,
            'level': self.level
        }

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = (
            'parent_category__name',
            'name',
        )