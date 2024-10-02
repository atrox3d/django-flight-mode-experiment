from django.core.management import call_command
from pathlib import Path
from fakedata.serializer import logger


from django.db.models import Model


def delete_initial_data(
        *dbmodels:Model
) -> None:
    for model in dbmodels:
        logger.info(f'deleting records from model {model.__qualname__}')
        model.objects.all().delete()


def reset_db(db_path='db.sqlite3'):
    if Path(db_path).exists():
        logger.info(f'{db_path} exists, deleting')
        Path(db_path).unlink()

    logger.info(f'migrating myapp')
    call_command('migrate', 'myapp')