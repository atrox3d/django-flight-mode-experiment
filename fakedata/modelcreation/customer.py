import logging
import random

from myapp.models import Customer
import myapp.models.Menu

logger = logging.getLogger(__name__)

weekdays = 'monday tuesday wednsday thursday friday saturday sunday'.split()
names = 'james john mary steven bob george jeff'.split()

def create_customers(
        customers:list[dict],
) -> list[myapp.models.Menu.Menu]:
    items = []
    for customer in customers:
        item = Customer.Customer(
            name = customer['name'],
            reservation_day = customer['reservation_day'],
            seats = customer['seats']
        )
        # logger.info(f'creating Menu for {item.menu_item}')
        item.save()
        items.append(item)
    return items
