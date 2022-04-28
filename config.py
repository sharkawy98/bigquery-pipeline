from os import path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# Local data
WORLD_CITIES = f'{basedir}/data/world_cities.csv'
API_CITIES = f'{basedir}/data/api_cities.csv'
