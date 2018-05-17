import requests
import json
from datetime import datetime
import numpy as np
import sys


def get_coordinates(city, street='', house=''):
    """
    Getting coordinates from Nominatim by city, street & house number.

    :param str city: city.
    :param str street: street.
    :param str house: house number.
    :return: latitude & longitude.
    :rtype: dict
    :raises SystemExit(2): if can not find specified address in Nominatim.
    :raises SystemExit(1): if connection with Nominatim failed.

    :Example:

    >>> get_coordinates('Санкт-Петербург')
    {'lat': '59.938732', 'lon': '30.316229'}
    """
    url = "http://nominatim.openstreetmap.org/search"

    street = '{} {}'.format(house, street)
    street = street.strip()

    querystring = {
        'q': city,
        'street': street,
        'format': 'json',
    }

    response = requests.get(url, params=querystring)

    if response.status_code == 200:
        ans = json.loads(response.text)

        if not ans:
            print('Can not find specified address.')
            sys.exit(2)

        coord_dict = {i: ans[0][i] for i in ans[0] if i in ['lon', 'lat']}

        return coord_dict

    else:
        print('Connection failed.')
        sys.exit(1)



def get_weather(coord_dict, token=None, test=True):
    """
    Getting weather from Open Weather Map by coordinates (needs token).

    :param dict coord_dict: latitude & logitude.
    :param str token: token to Open Weather Map API.
    :param bool test: if test=True, returns sample weather from OWM.
    :return: json answer from OpenWM server.
    :rtype: str
    :raises SystemExit(1): if connection with OpenWM failed.

    :Example:

    >>> get_weather({'lat': '59.938732', 'lon': '30.316229'}).keys()
    dict_keys(['cod', 'message', 'cnt', 'list', 'city'])
    """
    if test:
        url = "http://samples.openweathermap.org/data/2.5/forecast"
        querystring = {"lat":"35","lon":"139",
                       "appid":"b6907d289e10d714a6e88b30761fae22"}
    else:
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        querystring = coord_dict.update({'appid': token})

    response = requests.get(url, params=querystring)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print('Connection failed.')
        sys.exit(1)



def prepare_forecast(json_answer):
    """
    Prepare forecast for displaying.

    :param str json_answer: json answer from OpenWM server.
    :return: forecast + current weather, current date, city name.
    :rtype: tuple(dict, int, str)

    :Example:

    >>> prepare_forecast(get_weather({}))[2]
    'Tawarano'
    >>> prepare_forecast(get_weather({}))[1]
    30
    >>> prepare_forecast(get_weather({}))[0].keys()
    dict_keys([30, 31, 1, 2, 3, 4])
    """
    city = json_answer['city']['name']

    forecast = json_answer['list']

    five_days = {}

    days = []
    for cast in forecast:
        posixtime = cast['dt']
        day = int(datetime.fromtimestamp(posixtime).strftime('%d'))

        if day not in five_days:
            five_days[day] = {
                'temp': [],
                'pressure': [],
                'humidity': [],
                'clouds': [],
                'wind_speed': [],
                'description': [],
                'date': datetime.fromtimestamp(posixtime).strftime('%-d %B'),
            }
            days.append(day)

        main = cast['main']
        five_days[day]['temp'].append(main['temp'] - 273.15)
        five_days[day]['pressure'].append(main['pressure'])
        five_days[day]['humidity'].append(main['humidity'])
        five_days[day]['description'].append(cast['weather'][0]['description'])
        five_days[day]['clouds'].append(cast['clouds']['all'])
        five_days[day]['wind_speed'].append(cast['wind']['speed'])

    current_day = days[0]

    return five_days, current_day, city


def print_weather(weather_dict, current_day, city):
    """
    Print weather to console.

    :param dict weather_dict: weather.
    :param int current_day: current date.
    :param str city: city name.
    :return: console output.
    :rtype: text
    """
    current = weather_dict.pop(current_day)

    print('\n-- Weather in {} --\n'.format(city))

    print('Current:\n')
    print('{temp}°C, {descr}\n'
          'Humidity: {hum}%\n'
          'Pressure: {pres} hPa\n'
          'Cloudiness: {cloud}%\n'
          'Wind speed: {wind} m/s\n'.format(

        temp = round(current['temp'][0], 1),
        descr = current['description'][0],
        hum = int(np.mean(current['humidity'])),
        pres = int(np.mean(current['pressure'])),
        cloud = int(np.mean(current['clouds'])),
        wind = round(np.mean(current['wind_speed']), 1)
    ))


    print('\nForecast for 5 days:\n')

    for day in weather_dict:
        describe = weather_dict[day]['description']
        if len(set(describe)) > 1:
            start_desc = describe[0]
            while describe[-1] == start_desc:
                describe.pop(-1)
            end_desc = describe[-1]
            description = 'from {} to {}'.format(start_desc, end_desc)
        else:
            description = describe[0]

        print('-- {date} --\n\n'
              '{min_temp} - {max_temp}°C, {descr}\n'
              'Humidity: {hum}%\n'
              'Pressure: {pres} hPa\n'
              'Cloudiness: {cloud}%\n'
              'Wind speed: {wind} m/s\n'.format(

            date = weather_dict[day]['date'],
            min_temp = round(min(weather_dict[day]['temp']), 1),
            max_temp = round(max(weather_dict[day]['temp']), 1),
            descr = description,
            hum = int(np.mean(weather_dict[day]['humidity'])),
            pres = int(np.mean(weather_dict[day]['pressure'])),
            cloud = int(np.mean(weather_dict[day]['clouds'])),
            wind = round(np.mean(weather_dict[day]['wind_speed']), 1)
        ))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
