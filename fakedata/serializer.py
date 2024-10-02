import json
import logging


logger = logging.getLogger(__name__)

def save_to_json(
        filename:str, 
        data:list[dict],
        indent=2
) -> None:
    ''' save list of dicts to json '''

    logger.info(f'saving data to {filename}')
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=indent)


def load_from_json(
        filename:str
)-> list[dict]:
    ''' loads list of dicts from json '''

    logger.info(f'loading data from {filename}')
    with open(filename, 'r') as fp:
        return json.load(fp)


