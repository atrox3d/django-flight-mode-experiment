from ast import List
import logging

from . import dbtools
from . import menu
from . import customer

from myapp import models

logger = logging.getLogger(__name__)

def create_initial_data(
        json_menu_path:str='data/menu.json', 
        json_customers_path:str='data/customers.json', 
        reset_db=True,
        delete_existing=True,
) -> None:
    logger.info(f'{json_menu_path=}, {json_customers_path=}, {delete_existing=}')

    if reset_db:
        logger.info(f'resetting db')
        dbtools.reset_db()

    if delete_existing:
        logger.info(f'deleting existing data')
        dbtools.delete_initial_data(
            models.Menu, 
            models.MenuCategory, 
            models.MenuItems,
            models.Customer
        )
    
    data = dbtools.load_from_json(json_menu_path)
    categories = menu.get_categories_from_menu(data)
    menu_categories = menu.create_menu_categories(*categories)
    menu_items = menu.create_menu(data)

    data = dbtools.load_from_json(json_customers_path)
    customers = customer.create_customers(data)

