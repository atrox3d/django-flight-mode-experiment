from django.db import models

from myapp.models.menucategory import MenuCategory
from myapp.models.dictmixin import DictMixin
from myapp.models.menuitems import MenuItems

class Menu(models.Model, DictMixin):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        to=MenuCategory,
        on_delete=models.PROTECT,
        default=None,
        related_name='category_name'
    )

    def __str__(self) -> str:
        return f'{self.menu_item} - {self.category_id.menu_category_name}: {self.price}'

    def dict(self):
        return dict(
            menu_item=self.menu_item,
            price=self.price,
            category=self.category_id.menu_category_name,
        )

class Customer(models.Model, DictMixin):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    # def dict(self):
    #     return dict(
    #         name=self.name, 
    #         reservation_day=self.reservation_day,
    #         seats=self.seats,
    #     )

class Logger(models.Model, DictMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text='enter exact time')

    # def dict(self):
    #     return dict(
    #         first_name=self.first_name, 
    #         last_name=self.last_name, 
    #         time_log=self.time_log, 
    #     )
