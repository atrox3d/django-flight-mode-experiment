import json
import logging

from django.db.models import Model

logger = logging.getLogger(__name__)

def save_to_json(
        filename:str, 
        data:list[dict],
        indent=2
) -> None:
    logger.info(f'saving data to {filename}')
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=indent)


def load_from_json(
        filename:str
)-> list[dict]:
    logger.info(f'loading data from {filename}')
    with open(filename, 'r') as fp:
        return json.load(fp)


def delete_initial_data(
        *dbmodels:Model
) -> None:
    for model in dbmodels:
        logger.info(f'deleting records from model {model.__qualname__}')
        model.objects.all().delete()
