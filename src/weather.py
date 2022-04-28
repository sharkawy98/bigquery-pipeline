import requests
import pandas as pd
from config import API_CITIES



def get_cities_weather():
    '''Calling `MetaWeather: Location Endpoint` to get city's current 
    weather and 5 days forecast.

    ## Returns
    `DataFrame` of weather data to next 6 days for each city.
    '''
    api_cities = pd.read_csv(API_CITIES)
    weather = pd.DataFrame([])  # to hold api weather results

    for _, row in api_cities.iterrows():
        woeid = row['woeid']
        r = requests.get(f'https://www.metaweather.com/api/location/{woeid}')
        data = r.json()
        
        df = pd.DataFrame(data['consolidated_weather'])
        df['city'] = row['city']

        df = df[['city', 'applicable_date', 'the_temp', 'max_temp', 
                'min_temp', 'weather_state_name', 'wind_speed', 
                'wind_direction','wind_direction_compass',
                'air_pressure', 'humidity', 'visibility']]

        weather = pd.concat([weather, df], ignore_index=True)
    return weather
