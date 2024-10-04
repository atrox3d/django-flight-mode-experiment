from django.db import models

from myapp.models.dictmixin import DictMixin

class Logger(models.Model, DictMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text='enter exact time')
