# Weather Forecasts Batch Data Pipeline
__BigQuery pipeline__ is an implementation of an end-to-end batch data pipeline which runs in a weekly manner. It ingests the latest weather forecasts data from [MetaWeather API](https://www.metaweather.com/api/), loads that data to Google BigQuery and finally produces weather insights via a [dashboard](https://datastudio.google.com/reporting/15459279-7ad9-4186-8102-9e6fb0a62f2b).

The pipeline was built using __Python; Pandas; BigQuery API; Heroku CLI; Google Data Studio__


## Table of Contents
- [Architecture diagram](#architecture-diagram)
- [How it works](#how-it-works)
  - [Data pipeline](https://github.com/sharkawy98/bigquery-pipeline/edit/main/README.md#data-pipeline-%EF%B8%8F)
  - [Additional work](#additional-work)
- [Running project](#running-project)
- [Final results](#final-results)
  - [Dataset](#dataset)
  - [Dashboard](#dashboard)
- [References](#references)


## Architecture diagram
![diagram](https://user-images.githubusercontent.com/36075516/167403851-c253b860-ac5c-4c7a-a6e4-4d5d2ac5800d.png)


## How it works
### Data pipeline [↗️](src/__init__.py)
- __[Extract](src/weather.py):__ call [location endpoint](https://www.metaweather.com/api/#location) to get the current weather of a city and 5 days forecast
- __[Transform](src/transform.py):__ do some transformations like: renaming columns, changing data types, and generate a new date dimension table from the `date` column
- __[Load](src/load.py):__  load the final weather data and the generated dimension to bigquery
### Additional work
- __[Historical data](src/helpers/historical_weather.py):__ get history of weaher forecasts using [location day endpoint](https://www.metaweather.com/api/#locationday) between two selected dates 
- __[API cities](src/helpers/api_cities.py):__ get the cities available to query from MetaWeather API using [loaction search endpoint](https://www.metaweather.com/api/#locationsearch)
- __[Logging](src/helpers/log.py):__ implement simple custom logger using [loguru libirary](https://loguru.readthedocs.io/en/stable/)
- __Scheduling:__ run the pipeline in a weekly manner as the MetaWeather API provides forecasts for 6 days interval


## Running project
First, you should setup your google service account [permission](https://www.youtube.com/watch?v=gb0bytUGDnQ) and create the required tables using [BigQuery UI](https://console.cloud.google.com/bigquery)

Then clone this repo and run the pipeline
```sh
pip install -r requirements.txt

python main.py
```


## Final results
### Dataset
![dataset](https://user-images.githubusercontent.com/36075516/167303343-e8146e5f-1ec8-4658-8623-9d6c81dbe7c0.png)
### Dashboard
![dashboard](https://user-images.githubusercontent.com/36075516/167303387-fa7fc986-2951-4b9c-8887-93d6ac4dded1.jpg)


## References
* [BigQuery API Client Libraries](https://cloud.google.com/bigquery/docs/reference/libraries)
* [Heroku google application credentials buildpack](https://elements.heroku.com/buildpacks/buyersight/heroku-google-application-credentials-buildpack)
* [Scheduled Jobs with Custom Clock Processes in Python](https://devcenter.heroku.com/articles/clock-processes-python)
