import logging

from myapp import models

logger = logging.getLogger(__name__)

def get_categories_from_menu(
        menu:list[dict]
) -> list[str]:
    ''' extracts a list of categories from a list of dicts '''

    logger.info('extracting categories from menu')
    return list({menuitem['category'] for menuitem in menu})

def create_menu_categories(
        *categories
) -> list[models.MenuCategory]:
    ''' creates a list of MenuCategory objects from a list of categories '''

    logger.info(f'creating MenuCategory objects')
    return [models.MenuCategory.objects.create(menu_category_name=cat)
        for cat in categories]

def create_menu(
        menu:list[dict],
) -> list[models.Menu]:
    ''' creates Menu records using MEnuCategory records as foreign key '''
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
