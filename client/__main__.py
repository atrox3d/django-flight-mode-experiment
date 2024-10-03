from turtle import pos
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
)

SERVER = 'localhost'
PORT = 8000
ENDPOINT = 'logger'
URL = f'http://{SERVER}:{PORT}/{ENDPOINT}'
logging.info(f'{URL = }')

def get_csrftoken(url:str):
    logging.info(f'getting csfrtoken...')
    csrftoken = requests.get(URL).cookies['csrftoken']
    logging.info(f'{csrftoken = }')
    return csrftoken

def post(url:str, csrftoken:str, data:dict) -> requests.Response:
    header = {'X-CSRFToken': csrftoken}
    logging.info(f'setting {header = }')

    cookies = {'csrftoken': csrftoken}
    logging.info(f'setting {cookies = }')

    logging.info(f'setting {data = }')

    logging.info('sending POST request')
    response = requests.post(URL, data=data, headers=header, cookies=cookies)
    logging.info(f'{response = }')

    return response

data={
    'first_name': 'first',
    'last_name': 'last',
    'time_log': '11:11',
}
crsftoken = get_csrftoken(URL)
response = post(URL, crsftoken, data)
