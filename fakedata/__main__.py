import os
import django
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

if __name__ == '__main__':  

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s | %(message)s'
    )

    logger.info(f'fix DJANGO_SETTINGS_MODULE import')
    PROJECT_PATH = str(Path(__file__).parent.parent)
    sys.path.insert(0, PROJECT_PATH)

    logger.info(f'setting DJANGO_SETTINGS_MODULE')
    logger.info(f'current DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightmode.settings')

    logger.info(f'setting up django')
    django.setup()

    logger.info(f'importing data.data_creation')
    from fakedata import data

    logger.info(f'calling create_initial_data')
    data.create_initial_data()
