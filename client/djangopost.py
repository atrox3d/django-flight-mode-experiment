import requests
import logging


logger = logging.getLogger(__name__)

def get_csrftoken(url:str):
    logger.info(f'getting csfrtoken...')
    csrftoken = requests.get(url).cookies['csrftoken']
    logger.info(f'{csrftoken = }')
    return csrftoken


def post(url:str, csrftoken:str, data:dict) -> requests.Response:
    header = {'X-CSRFToken': csrftoken}
    logger.info(f'setting {header = }')

    cookies = {'csrftoken': csrftoken}
    logger.info(f'setting {cookies = }')

    logger.info(f'setting {data = }')

    logger.info('sending POST request')
    response = requests.post(url, data=data, headers=header, cookies=cookies)
    logger.info(f'{response = }')

    return response