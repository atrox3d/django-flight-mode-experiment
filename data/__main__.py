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

    logger.info(f'importing myapp.helpers.db')
    from data import data_creation

    logger.info(f'calling create_initial_data')
    data_creation.create_initial_data()
