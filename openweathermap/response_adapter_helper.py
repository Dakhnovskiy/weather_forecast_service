import datetime


def response_adapter(response_data, max_date):
    for row in response_data['list']:
        dt_row = datetime.datetime.fromtimestamp(row['dt'])
        if dt_row > max_date:
            continue

        row['dt_txt'] = dt_row.strftime('%d.%m.%Y %H:%M')
        yield row
