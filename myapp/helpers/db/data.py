from ast import List
import logging

from myapp.helpers.db.management import load_json_menu
from myapp.helpers.db.management import delete_initial_data
from myapp.helpers.db.menu import get_categories_from_menu
from myapp.helpers.db.menu import create_menu_categories
from myapp.helpers.db.menu import create_menu_items

from ... import models

logger = logging.getLogger(__name__)

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
