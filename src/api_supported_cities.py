import requests
import pandas as pd
from config import WORLD_CITIES



def get_api_cities_with_woeid():
    '''The MetaWeatherApi support few number of cities
    all over the world, So I used `MetaWeather: Location Searh Endpoint`
    to get API's supported cities alongside `woeid`.

    `woeid`: aka. where on earth, is a unique identifier for each city

    ## Returns
    `DataFrame` of API's supported cities.
    '''
    all_cities = pd.read_csv(WORLD_CITIES)

    def get_woeid(city):
        r = requests.get(
            f'https://www.metaweather.com/api/location/search/?query={city}'
        )
        if r.json():  # identify supported cities
            data = r.json()[0]
            return str(data['woeid'])
    all_cities['woeid'] = all_cities['city'].apply(get_woeid)
    
    api_cities = all_cities[all_cities['woeid'].notna()].reset_index(drop=True)
    return api_cities


api_cities = get_api_cities_with_woeid()
print(api_cities)

api_cities.to_csv('api_cities.csv', index=False)
