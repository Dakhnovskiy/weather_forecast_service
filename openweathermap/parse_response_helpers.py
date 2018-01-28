from .response_adapter_helper import response_adapter


def parse_response_row(response_row):
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


def parse_response(response, max_date):
    weather_description_list = []
    for row in response_adapter(response, max_date):
        weather_description_list.append(parse_response_row(row))

    return '\n\n'.join(weather_description_list)
