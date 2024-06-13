from django.db import models


# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.title, self.length)
