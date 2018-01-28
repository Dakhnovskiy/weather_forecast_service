import os


class Config(object):
    DEBUG = False

    MAX_COUNT_DAYS_FOR_FORECAST = 5

    API_ENDPOINT = 'http://api.openweathermap.org'
    API_KEY = os.environ.get('OPENWEATHERMAP_KEY')
    API_FUNCTION_WEATHER_FORECAST = 'data/2.5/forecast'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
