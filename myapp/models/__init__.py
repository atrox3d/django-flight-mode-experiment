from django.db import models

from myapp.models.dictmixin import DictMixin
from myapp.models.menuitems import MenuItems
from myapp.models.menucategory import MenuCategory
from myapp.models.menu import Menu
from myapp.models.customer import Customer
from myapp.models.logger import Logger

    # def dict(self):
    #     return dict(
    #         name=self.name, 
    #         reservation_day=self.reservation_day,
    #         seats=self.seats,
    #     )

# class Logger(models.Model, DictMixin):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     time_log = models.TimeField(help_text='enter exact time')

    # def dict(self):
    #     return dict(
    #         first_name=self.first_name, 
    #         last_name=self.last_name, 
    #         time_log=self.time_log, 
    #     )
