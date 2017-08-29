from django.db import models

class Author(models.Model):
    name = models.TextField(max_length=200, null=False)
    image_url = models.TextField(max_length=300, null=True)
    description = models.TextField(max_length=800, null=False)

class Tag(models.Model):
    name = models.TextField(max_length=200, null=False)
    level = models.IntegerField()

class Category(models.Model):
    name = models.TextField(max_length=200, null=False)
    parent_category = models.ForeignKey('self', null=True)
    level = models.IntegerField()

class MusicTrack(models.Model):
    name = models.TextField(max_length=200, null=False)
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    short_description = models.TextField(max_length=120, null=False)
    long_description = models.TextField(max_length=300, null=False)
    duration = models.TimeField(null=False)
    image_url = models.TextField(max_length=300, null=True)

class MusicTrackTag(models.Model):
    track = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tag = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)

class MusicTrackCategory(models.Model):
    track = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)
