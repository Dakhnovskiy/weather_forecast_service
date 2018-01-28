import os
from flask import Flask
from views import WeatherForecastServiceView

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)


limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=['20 per minute']
)

app.add_url_rule(
    '/v1/forecast/',
    view_func=WeatherForecastServiceView.as_view('weather_forecast'),
    methods=['GET']
)

app.config.from_object(os.environ.get('WEATHER_CONFIG'))


if __name__ == '__main__':
    app.run()
