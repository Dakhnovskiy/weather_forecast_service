from marshmallow import Schema, fields


class WeatherForecastSchema(Schema):
    city = fields.Str(required=True)
    count_days = fields.Integer(required=False, allow_none=True, missing=lambda: None)
