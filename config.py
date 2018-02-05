import os


class Config(object):
    DEBUG = False
    JSON_AS_ASCII = False

    API_ENDPOINT = 'http://api.openweathermap.org'
    API_KEY = os.environ.get('OPENWEATHERMAP_KEY')
    API_FUNCTION_WEATHER_FORECAST = 'data/2.5/forecast'
    API_FUNCTION_WEATHER_CURRENT = 'data/2.5/weather'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
