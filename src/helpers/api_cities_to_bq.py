from pandas import read_csv
from config import API_CITIES
from src.load import load_to_bigquery


# Act as enrichment data
city_dim = read_csv(API_CITIES)
load_to_bigquery(city_dim, 'forecasts', 'city')
