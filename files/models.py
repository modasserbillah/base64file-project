from django.db import models


class File(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    path = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title
