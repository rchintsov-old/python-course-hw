import requests
import json
from datetime import datetime
import numpy as np
import sys


def get_adress():
    while True:

        city = input('Введите город > ')
        try:
            float(city)
            print('Неверный ввод, попробуйте еще раз.')
            continue
        except ValueError:
            pass

        street = input('Введите улицу (опционально) > ')
        try:
            float(street)
            print('Неверный ввод, попробуйте еще раз.')
            continue
        except ValueError:
            pass

        house = input('Введите дом (опционально) > ')
        try:
            house = int(house)
        except ValueError:
            print('Неверный ввод, попробуйте еще раз.')
            continue

        return city, street, house



def get_coordinates(city, street, house):

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
            print('Невозможно найти данный адрес.')
            sys.exit(2)

        coord_dict = {i: ans[0][i] for i in ans[0] if i in ['lon', 'lat']}

        return coord_dict

    else:
        print('Не удается установить соединение.')
        sys.exit(2)



def get_weather(coord_dict, token=None, test=True):

    if test:
        url = "http://samples.openweathermap.org/data/2.5/forecast"
        querystring = {"lat":"35","lon":"139","appid":"b6907d289e10d714a6e88b30761fae22"}
    else:
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        querystring = coord_dict.update({'appid': token})

    response = requests.get(url, params=querystring)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print('Не удается установить соединение.')
        sys.exit(2)



def prepare_forecast(json_answer):

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
                'date': datetime.fromtimestamp(posixtime).strftime('%d %B'),
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

    current = weather_dict.pop(current_day)

    print('\nCurrent weather in {}:'.format(city))

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

        print('\n-- {date} --\n'
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

