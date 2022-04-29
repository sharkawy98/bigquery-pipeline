from config import load_dotenv
from .weather import get_cities_weather
from .transform import transform_weather, generate_date_dim
from .load import load_to_bigquery
from .helpers.log import LOGGER



def init_pipeline():
    '''Initiating the whole ETL data pipeline.
    '''
    try:
        # extract weather data
        LOGGER.info('Start ingesting weather data from <Location Endpoint>')
        weather = get_cities_weather()
        LOGGER.success(f'Successfully extracted data to <DataFrame> with {len(weather)} rows')

        # transformations => weather, date_dim
        LOGGER.info('Doing some transformations to the <weather_df>')
        weather = transform_weather(weather)
        date_dim = generate_date_dim(weather)

        # load to bigquery
        LOGGER.info('Loading data to <forecasts.weather> BigQuery table')
        load_job = load_to_bigquery(weather, 'forecasts', 'weather')
        LOGGER.success(load_job.result())
        
        LOGGER.info('Loading data to <forecasts.date> BigQuery table')
        load_job = load_to_bigquery(date_dim, 'forecasts', 'date')
        LOGGER.success(load_job.result())
    except Exception as e:
        LOGGER.error(f"Unexpected error occurred: {e}")
