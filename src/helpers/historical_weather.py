import pandas as pd
import requests
from datetime import date, timedelta

from config import API_CITIES
from transform import transform_weather, generate_date_dim
from load import load_to_bigquery




def get_weather_history(start_date, end_date):
    '''Calling `MetaWeather: Location Day Endpoint` to extracts weather 
    for a particular location & date.

    ## Returns
    `DataFrame` of cities weather history from `start_date` to `end_date`
    '''
    historical_weather = pd.DataFrame([])
    cities = pd.read_csv(API_CITIES)
    
    for _, row in cities.iterrows():
        start = start_date
        end = end_date
        add_day = timedelta(days=1)
        
        while start < end:
            # ex. https://metaweather.com/api/location/44418/2013/4/27/
            endpoint = 'https://www.metaweather.com/api/location/'
            + str(row['woeid']) + '/'
            + '/'.join(str(start).split('-'))
            
            r = requests.get(endpoint)
            data = r.json()[0]

            df = pd.DataFrame([data])
            df['city'] = row['city']
            df = df[['city', 'applicable_date', 'the_temp', 'max_temp', 
                    'min_temp', 'weather_state_name', 'wind_speed', 
                    'wind_direction','wind_direction_compass',
                    'air_pressure', 'humidity', 'visibility']]

            historical_weather = pd.concat(
                [historical_weather, df],
                ignore_index=True
            )
            start += add_day

    return transform_weather(historical_weather)



# historical_weather = get_weather_history(date(2022, 1, 1), date.today())
# date_dim = generate_date_dim(historical_weather)

# load_to_bigquery(historical_weather, 'forecasts', 'weather')
# load_to_bigquery(date_dim, 'forecasts', 'date')
