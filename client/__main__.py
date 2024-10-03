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

logging.info(f'getting csfrtoken...')
csrftoken = requests.get(URL).cookies['csrftoken']
logging.info(f'{csrftoken = }')

header = {'X-CSRFToken': csrftoken}
logging.info(f'setting {header = }')

cookies = {'csrftoken': csrftoken}
logging.info(f'setting {cookies = }')

data={
    'first_name': 'first',
    'last_name': 'last',
    'time_log': '11:11',
}
logging.info(f'setting {data = }')

logging.info('sending POST request')
response = requests.post(URL, data=data, headers=header, cookies=cookies)
logging.info(f'{response = }')
