from django.db import models

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    img_path = models.CharField(max_length=1200, null=True)

    def __str__(self):
        return self.name
