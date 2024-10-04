import logging

from myapp import models
import myapp.models.MenuCategory

logger = logging.getLogger(__name__)

def get_categories_from_menu(
        menu:list[dict]
) -> list[str]:
    logger.info('extracting categories from menu')
    return list({menuitem['category'] for menuitem in menu})

def create_menu_categories(
        *categories
) -> list[myapp.models.MenuCategory.MenuCategory]:
    logger.info(f'creating MenuCategory objects')
    return [myapp.models.MenuCategory.MenuCategory.objects.create(menu_category_name=cat)
        for cat in categories]

def create_menu_items(
        menu:list[dict],
        # categories:list[models.MenuCategory]
) -> list[models.Menu]:
    items = []
    for menuitem in menu:
        category = myapp.models.MenuCategory.MenuCategory.objects.filter(
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
