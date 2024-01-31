from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.id