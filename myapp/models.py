from django.db import models

# Create your models here.

class MenuItems(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
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