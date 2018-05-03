import requests


def get(city='London,uk', tk=''):

    url = "http://samples.openweathermap.org/data/2.5/weather"

    querystring = {
        "q":"London,uk",
        "appid":"b6907d289e10d714a6e88b30761fae22"}

    response = requests.get(url, params=querystring)

    data = response.json()

    print('Now in {} {}'.format(city, data['weather'][0]['description']))


def get_forecast(city, tk):

    url = "http://samples.openweathermap.org/data/2.5/weather"

    querystring = {
        "q": city,
        "appid": tk}

    response = requests.get(url, params=querystring)

    data = response.json()

    print('Now in {} {}'.format(city, data['weather'][0]['description']))


# разделить получение данных и вывод данных
