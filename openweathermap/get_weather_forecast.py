import posixpath
import requests


def get_weather_forecast(api_endpoint, api_function, api_key, country, city):
    """
    Получть данные о погоде от внешнего сервиса
    :param api_endpoint: хост сервиса
    :param api_function: функция запроса прогноза погоды на сервисе
    :param api_key: ключ для интеграции с сервисом
    :param country: код страны
    :param city: город
    :return: ответ от сервиса (словарь)
    """
    city_for_find = '%s,%s' % (city, country)

    request_url = posixpath.join(api_endpoint, api_function)
    request_params = {'q': city_for_find, 'units': 'metric', 'lang': 'ru', 'APPID': api_key}

    response = requests.get(request_url, params=request_params)
    return response.json()

