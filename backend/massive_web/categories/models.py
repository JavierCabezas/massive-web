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

    def family(self):
        '''
        Returns a list of identifiers of all the family of this cateogry
        family means:
            a) If the tags is a parent it returns an array with its id and the id of all of their children.
            b) If the tag is a child it return an array with its id, the id of all of its brothers and the one of the parent.
        :return:
        '''
        if self.level == 1:
            cats = Category.objects.filter(parent_category_id=self.id)
            out = [c.id for c in cats]
            out.append(self.id)
        else:
            cats = Category.objects.filter(parent_category_id=self.parent_category_id)
            out = [c.id for c in cats]
            out.append(self.parent_category_id)

        return out
