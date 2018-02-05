import datetime
from .response_adapter_helper import response_adapter


def get_description_weather_by_response_row(response_row):
    """
    Получить описание погоды по строке ответа сервиса
    :param response_row: строка ответа сервиса
    :return: описание погоды
    """
    dt_txt = response_row['dt_txt']
    temp = '{0:+3.0f}'.format(response_row['main']['temp'])
    weather_description = response_row['weather'][0]['description']
    wind_speed = response_row['wind']['speed']
    return '{date}:\nТемпература: {temp}°С\n{descr}\nCкорость ветра: {wind_speed} м/с'.format(
        date=dt_txt,
        temp=temp,
        descr=weather_description,
        wind_speed=wind_speed
    )


def parse_response_weather_forecast(response_data, max_date):
    """
    Парсинг ответа прогноза на несколько дней
    :param response_data: ответ сервиса (словарь)
    :param max_date: дата до которой необходимо отфильтровать данные
    :return: описание погоды
    """

    weather_description_list = []
    for row in response_adapter(response_data, max_date):
        weather_description_list.append(get_description_weather_by_response_row(row))

    return '\n\n'.join(weather_description_list)


def parse_response_weather_current(response_data):
    """
    Парсинг ответа прогноза на один день
    :param response_data: ответ сервиса (словарь)
    :return: описание погоды
    """
    if 'main' in response_data:
        response_data['dt_txt'] = 'Сегодня'
        return get_description_weather_by_response_row(response_data)


def parse_response(response_data, count_days_for_forecast):
    """
    Парсинг ответа прогноза
    :param response_data: ответ сервиса (словарь)
    :param count_days_for_forecast: количество дней, за которое необходим прогноз или None
    :return: описание погоды
    """
    response_not_found_msg = 'К сожалению, по вашему запросу данных не найдено'
    max_count_days_for_forecast = 5

    if count_days_for_forecast:
        count_days = min(max_count_days_for_forecast, count_days_for_forecast)
        max_date = datetime.datetime.today() + datetime.timedelta(days=count_days)
        weather_description = parse_response_weather_forecast(response_data, max_date)
    else:
        weather_description = parse_response_weather_current(response_data)

    return weather_description or response_not_found_msg
