from flask import jsonify, current_app
from flask import request
from flask.views import View

import datetime

from openweathermap import get_weather_forecast, parse_response
from validators import WeatherForecastSchema


class WeatherForecastServiceView(View):

    def dispatch_request(self, **kwargs):
        method_name = request.method.lower()
        return getattr(self, method_name)(**kwargs)

    def get(self):
        max_count_days_for_forecast = current_app.config['MAX_COUNT_DAYS_FOR_FORECAST']
        api_endpoint = current_app.config['API_ENDPOINT']
        api_key = current_app.config['API_KEY']
        api_function_weather_forecast = current_app.config['API_FUNCTION_WEATHER_FORECAST']

        args, errors = WeatherForecastSchema().load(request.args)
        if errors:
            response = jsonify(errors)
            response.status_code = 400
            return response

        city = args['city']
        count_days_for_forecast = args['count_days']

        country = 'RU'
        count_days = min(max_count_days_for_forecast, count_days_for_forecast)
        max_date = datetime.datetime.today() + datetime.timedelta(days=count_days)

        response_json = get_weather_forecast(
            api_endpoint,
            api_function_weather_forecast,
            api_key,
            country,
            city
        )

        weather_description = parse_response(response_json, max_date)

        response_dict = {
            'description': 'Прогноз погоды в населенном пункте {0}\n{1}'.format(
                city,
                weather_description
            )
        }
        return jsonify(response_dict)
