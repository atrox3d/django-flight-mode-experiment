from django.contrib import admin

# Register your models here.

from .models import (
    Logger, 
    MenuItems, 
    MenuCategory, 
    Menu, 
    Customer,
    Reservation
)

admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(MenuItems)
admin.site.register(Logger)
admin.site.register(Reservation)
