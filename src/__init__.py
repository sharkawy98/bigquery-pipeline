from config import load_dotenv
from .weather import get_cities_weather
from .transform import transform_weather, generate_date_dim
from .load import load_to_bigquery



def init_pipeline():
    '''Initiating the whole ETL data pipeline.
    '''
    # extract weather data
    weather = get_cities_weather()

    # transformations => weather, date_dim
    weather = transform_weather(weather)
    date_dim = generate_date_dim(weather)

    # load to bigquery
    load_to_bigquery(weather, 'forecasts', 'weather')
    load_to_bigquery(date_dim, 'forecasts', 'date')
