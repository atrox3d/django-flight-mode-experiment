from django.contrib import admin

# Register your models here.

from .models import Customer, Menu, Logger, MenuItems, MenuCategory

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(MenuItems)
admin.site.register(Logger)
