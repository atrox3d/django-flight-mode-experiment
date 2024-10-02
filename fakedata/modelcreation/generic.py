import logging
from django.db import models

logger = logging.getLogger(__name__)

def create_objects(
        data:list[dict],
        model:models.Model
) -> list[models.Model]:
    ''' creates list of models from a list of dicts '''

    objects = []
    for item in data:
        object = model(**item)
        object.save()
        objects.append(object)
    return objects
