from myapp.models.dictmixin import DictMixin


from django.db import models


class Customer(models.Model, DictMixin):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self) -> str:
        return self.name