from myapp.models.dictmixin import DictMixin


from django.db import models


class MenuCategory(models.Model, DictMixin):
    menu_category_name = models.CharField(max_length=200)