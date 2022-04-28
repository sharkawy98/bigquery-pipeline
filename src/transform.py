import pandas as pd



def transform_weather(weather):
    '''## Returns
    `DataFrame` of weather after some transformations.
    '''
    # rename columns with meaningful names with measurement units
    weather = weather.rename(columns={
        'applicable_date': 'date', 
        'the_temp': 'avg_temp_c',
        'max_temp': 'max_temp_c',
        'min_temp': 'min_temp_c',
        'weather_state_name': 'weather_condition',
        'wind_speed': 'wind_speed_mph',
        'wind_direction': 'wind_direction_degrees',
        'air_pressure': 'air_pressure_mbar',
        'humidity': 'humidity_percent',
        'visibility': 'visibility_miles'
    })

    weather['date'] = pd.to_datetime(weather['date'])  # convert to date
    weather = weather.round()  # round all floats
    
    return weather
