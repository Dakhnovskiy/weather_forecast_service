import posixpath
import requests


def get_weather_forecast(api_endpoint, api_function, api_key, country, city):

    city_for_find = '%s,%s' % (city, country)

    request_url = posixpath.join(api_endpoint, api_function)
    request_params = {'q': city_for_find, 'units': 'metric', 'lang': 'ru', 'APPID': api_key}

    response = requests.get(request_url, params=request_params)
    return response.json()

