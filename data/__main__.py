import os
import django
import logging


logger = logging.getLogger(__name__)

if __name__ == '__main__':  

    logging.basicConfig(
        level=logging.DEBUG
    )
    logger.info(f'setting DJANGO_SETTINGS_MODULE')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightmode.settings')

    logger.info(f'setting up django')
    django.setup()

    logger.info(f'importing data.data_creation')
    from data import data_creation, dbtools

    logger.info(f'resetting db')
    dbtools.reset_db()

    logger.info(f'calling create_initial_data')
    data_creation.create_initial_data()
