from django.db import models

from myapp.models.dictmixin import DictMixin


class MenuItems(models.Model, DictMixin):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()
