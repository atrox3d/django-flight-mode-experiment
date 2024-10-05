from django.db import models

from myapp.models.dictmixin import DictMixin


class Reservation(models.Model, DictMixin):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'