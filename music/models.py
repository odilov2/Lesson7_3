from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    search = models.IntegerField(default=0)
    member = models.IntegerField(default=0)


class Albom(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField(null=True)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    songs_count = models.IntegerField(default=0)


class Songs(models.Model):
    title = models.CharField(max_length=40)
    cover = models.URLField(null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    listened = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]
