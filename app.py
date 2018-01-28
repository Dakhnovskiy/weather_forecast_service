import os
from flask import Flask
from views import WeatherForecastServiceView


app = Flask(__name__)


app.add_url_rule(
    '/forecast/',
    view_func=WeatherForecastServiceView.as_view('weather_forecast'),
    methods=['GET']
)

app.config.from_object(os.environ.get('WEATHER_CONFIG'))


if __name__ == '__main__':
    app.run()
