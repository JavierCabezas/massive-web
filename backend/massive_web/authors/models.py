from django.db import models


class Author(models.Model):
    name = models.TextField(
        max_length=200,
        null=False
    )

    image = models.ImageField(
        upload_to='authors',
        null=True,
    )

    description = models.TextField(
        max_length=800,
        null=False
    )

    description_es = models.TextField(
        max_length=800,
        null=False
    )

    def __str__(self):
        return self.name

    def admin_image(self):
        return '<img src="%s"/>' % self.image.url

    admin_image.allow_tags = True

    @staticmethod
    def id_dict():
        """
        Returns a dictionary with all the objects of this class instance
        :return: Dictionary in the format { id: Author instance model , id:MusicPack instance 2... }
        """
        out = {}
        for a in Author.objects.all():
            out[a.id] = a
        return out


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'