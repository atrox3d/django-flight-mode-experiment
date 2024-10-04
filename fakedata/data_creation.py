import logging
from pathlib import Path

import myapp.models.MenuItems


from . import db
from . import serializer
from .modelcreation import menu
from .modelcreation import customer
from .modelcreation import generic

from myapp import models

logger = logging.getLogger(__name__)

JSON = Path(__file__).parent / 'json'

def create_initial_data(
        json_menu_path:str=f'{JSON}/menu.json', 
        json_customers_path:str=f'{JSON}/customers.json', 
        reset_db=True,
        delete_existing=True,
) -> None:
    ''' creates data into db from json files '''

    logger.info(f'{json_menu_path=}, {json_customers_path=}, {delete_existing=}')

    if reset_db:
        logger.info(f'resetting db')
        db.reset_db()

    if delete_existing:
        logger.info(f'deleting existing data')
        db.delete_initial_data(
            models.Menu, 
            models.MenuCategory, 
            myapp.models.MenuItems.MenuItems,
            models.Customer,
            models.Logger
        )
    
    data = serializer.load_from_json(json_menu_path)
    categories = menu.get_categories_from_menu(data)
    menu_categories = menu.create_menu_categories(*categories)
    menu_items = menu.create_menu(data)

    data = serializer.load_from_json(json_customers_path)
    customers = generic.create_objects(data, models.Customer)

