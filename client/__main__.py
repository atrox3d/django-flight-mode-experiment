from pathlib import Path
import logging
import sys
import os

# PROJECT_PATH = str(Path(__file__).parent.parent)
# sys.path.insert(0, '.')
# sys.path.insert(0, '..')
# sys.path.insert(0, 'client')

for path in sys.path:
    print(f'{path = }')

from djangopost import post
from djangopost import get_csrftoken

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

logger.info(f'{os.getcwd() = }')

SERVER = 'localhost'
PORT = 8000
ENDPOINT = 'logger'
URL = f'http://{SERVER}:{PORT}/{ENDPOINT}'
logger.info(f'{URL = }')

data={
    'first_name': 'first',
    'last_name': 'last',
    'time_log': '11:11',
}
crsftoken = get_csrftoken(URL)
response = post(URL, crsftoken, data)
