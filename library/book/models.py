from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField (blank=True)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name    