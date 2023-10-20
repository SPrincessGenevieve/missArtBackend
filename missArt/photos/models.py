from django.db import models

class Photos(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return "Photos"

