from django.db import models

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    # img_path = models.CharField(max_length=1200, null=True)
    img_path = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    released = models.CharField(max_length=5)
    language = models.CharField(max_length=20)
    # album_id = models.CharField(max_length=10, null=True)
    file=models.FileField(null=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=100)
    # Adress
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Students(models.Model):
    song = models.ForeignKey(
        Song, on_delete=models.SET_NULL, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)

    def __str__(self):
        return self.name
