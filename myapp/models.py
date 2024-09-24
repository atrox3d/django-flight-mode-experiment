from django.db import models

# Create your models here.

class MenuItems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()
