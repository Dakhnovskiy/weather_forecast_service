import datetime


def response_adapter(response_data, max_date):
    """
    Преобразование ответа от сервиса http://api.openweathermap.org/data/2.5/forecast
    Преобразует данные поля dt_txt в необходимый формат
    :param response_data: ответ от сервиса (словарь)
    :param max_date: дата до которой необходимо отфильтровать данные
    """
    if 'list' in response_data:
        for row in response_data['list']:
            dt_row = datetime.datetime.fromtimestamp(row['dt'])
            if dt_row > max_date:
                continue

            row['dt_txt'] = dt_row.strftime('%d.%m.%Y %H:%M')
            yield row
