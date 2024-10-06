import logging
from pathlib import Path

from django.contrib.auth.models import User

from .. import db
from .. import loader
from . import menu
from . import customer
from . import generic

import myapp.models


logger = logging.getLogger(__name__)

JSON = Path(__file__).parent.parent / 'json'

def create_initial_data(
        json_menu_path:str=f'{JSON}/menu.json', 
        json_customers_path:str=f'{JSON}/customers.json',
        json_users_path:str=f'{JSON}/users.json',
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
            myapp.models.Menu, 
            myapp.models.MenuCategory, 
            myapp.models.MenuItems,
            myapp.models.Customer,
            myapp.models.Logger
        )
    
    menu_data = loader.load_from_json(json_menu_path)
    categories = menu.get_categories_from_menu(menu_data)
    menu_categories = menu.create_menu_categories(*categories)
    menu_items = menu.create_menu(menu_data)

    customers_data = loader.load_from_json(json_customers_path)
    customers = generic.create_objects(customers_data, myapp.models.Customer)

    users_data = loader.load_from_json(json_users_path)
    users = generic.create_objects(users_data, User)
    
    # admin = User.objects.create_superuser('admin', 'admin@admin', 'admin')
    # admin.is_superuser = True
    # admin.is_staff = True
    # admin.save()

