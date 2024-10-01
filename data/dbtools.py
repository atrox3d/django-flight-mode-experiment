import json
import logging

from django.db.models import Model

logger = logging.getLogger(__name__)

def save_json_menu(
        filename:str, menu:list[dict]
) -> None:
    with open(filename, 'w') as fp:
        json.dump(menu, fp, indent=2)


def load_json_menu(
        filename:str
)-> list[dict]:
    logger.info(f'loading menu from {filename}')
    with open(filename, 'r') as fp:
        return json.load(fp)


def delete_initial_data(
        *dbmodels:Model
) -> None:
    for model in dbmodels:
        logger.info(f'deleting records from model {model.__qualname__}')
        model.objects.all().delete()
