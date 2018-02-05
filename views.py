from flask import jsonify, current_app
from flask import request
from flask.views import View

from openweathermap import get_weather_forecast, parse_response
from validators import WeatherForecastSchema


class WeatherForecastServiceView(View):

    def dispatch_request(self, **kwargs):
        method_name = request.method.lower()
        return getattr(self, method_name)(**kwargs)

    def get(self):
        api_endpoint = current_app.config['API_ENDPOINT']
        api_key = current_app.config['API_KEY']

        args, errors = WeatherForecastSchema().load(request.args)
        if errors:
            response = jsonify(errors)
            response.status_code = 400
            return response

        city = args['city']
        count_days_for_forecast = args['count_days']
        api_function = self.__get_api_function_by_count_days(count_days_for_forecast)

        country = 'RU'

        response_json = get_weather_forecast(
            api_endpoint,
            api_function,
            api_key,
            country,
            city
        )

        weather_description = parse_response(response_json, count_days_for_forecast)

        response_dict = {
            'description': 'Прогноз погоды в населенном пункте {0}\n{1}'.format(
                city,
                weather_description
            )
        }
        return jsonify(response_dict)

    @staticmethod
    def __get_api_function_by_count_days(count_days):
        api_function = current_app.config['API_FUNCTION_WEATHER_CURRENT']

        if count_days:
            api_function = current_app.config['API_FUNCTION_WEATHER_FORECAST']
        return api_function
