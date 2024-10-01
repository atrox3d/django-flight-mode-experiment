from ast import List
import logging

# from .management import load_json_menu
# from .management import delete_initial_data
from . import management
from .menu import get_categories_from_menu
from .menu import create_menu_categories
from .menu import create_menu_items

from ... import models

logger = logging.getLogger(__name__)

def create_initial_data(
        json_menu_path:str='menu.json', 
        delete_existing=True
) -> None:
    logger.info(f'{json_menu_path=}, {delete_existing=}')
    if delete_existing:
        management.delete_initial_data(
            models.Menu, 
            models.MenuCategory, 
            models.MenuItems
        )
    
    menu = management.load_json_menu(json_menu_path)
    categories = get_categories_from_menu(menu)
    menu_categories = create_menu_categories(*categories)
    menu_items = create_menu_items(menu)
