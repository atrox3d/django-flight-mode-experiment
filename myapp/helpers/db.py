from ast import List
from django.db.models import Model
import json
import logging

from .. import models

logger = logging.getLogger(__name__)

def save_json_menu(
        filename:str, menu:list[dict]
) -> None:
    with open(filename, 'w') as fp:
        json.dump(menu, fp, indent=2)

def load_json_menu(
        filename:str
)-> list[dict]:
    logger.info(f'loading menu from {filename}')
    with open(filename, 'r') as fp:
        return json.load(fp)

def delete_initial_data(
        *dbmodels:Model
) -> None:
    for model in dbmodels:
        logger.info(f'deleting records from model {model.__qualname__}')
        model.objects.all().delete()
    
def get_categories_from_menu(
        menu:list[dict]
) -> list[str]:
    logger.info('extracting categories from menu')
    return list({menuitem['category'] for menuitem in menu})

def create_menu_categories(
        *categories
) -> list[models.MenuCategory]:
    logger.info(f'creating MenuCategory objects')
    return [models.MenuCategory.objects.create(menu_category_name=cat) 
        for cat in categories]

def create_menu_items(
        menu:list[dict], 
        # categories:list[models.MenuCategory]
) -> list[models.Menu]:
    items = []
    for menuitem in menu:
        category = models.MenuCategory.objects.filter(
                menu_category_name=menuitem['category']
            ).first()
        item = models.Menu(
            menu_item = menuitem['menu_item'],
            price = menuitem['price'],
            category_id = category
        )
        logger.info(f'creating Menu for {item.menu_item}')
        item.save()
        items.append(item)
    return items

def create_initial_data(
        json_menu_path:str='menu.json', delete_existing=True
) -> None:
    logger.info(f'{json_menu_path=}, {delete_existing=}')
    if delete_existing:
        delete_initial_data(
            models.Menu, 
            models.MenuCategory, 
            models.MenuItems
        )
    
    menu = load_json_menu(json_menu_path)
    categories = get_categories_from_menu(menu)
    menu_categories = create_menu_categories(*categories)
    menu_items = create_menu_items(menu)
