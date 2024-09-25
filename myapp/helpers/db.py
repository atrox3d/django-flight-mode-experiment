from django.db.models import Model
from .. import models


def delete_initial_data(*dbmodels:Model):
    for model in dbmodels:
        model.objects.all().delete()
    
    create_menu_categories()


def create_menu_categories():
    categories = 'italian greek turklish'.split()
    [models.MenuCategory.objects.create(menu_category_name=cat) 
        for cat in categories]

def create_initial_data(delete_existing=True):
    if delete_existing:
        delete_initial_data(
            models.Menu, 
            models.MenuCategory, 
            models.MenuItems
        )
    


