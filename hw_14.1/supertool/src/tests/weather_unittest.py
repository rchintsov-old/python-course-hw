import unittest
from supertool import weather
    

class TestGetCoordinates(unittest.TestCase):

    def test_get_coordinates_positive(self):
        self.assertEqual(weather.get_coordinates('Санкт-Петербург'), {'lat': '59.938732', 'lon': '30.316229'}, "Wrong answer")


class TestGetWeather(unittest.TestCase):

    def test_get_weather_positive(self):
        self.assertEqual(weather.get_weather({'lat': '59.938732', 'lon': '30.316229'}).keys(), dict_keys(['cod', 'message', 'cnt', 'list', 'city']), "Wrong answer")


class TestPrepareForecast(unittest.TestCase):

    def test_prepare_forecast_positive(self):
        self.assertEqual(weather.prepare_forecast(get_weather({}))[2], 'Tawarano', "Wrong answer")


    def test_prepare_forecast_positive_2(self):
        self.assertEqual(weather.prepare_forecast(get_weather({}))[1], 30, "Wrong answer")


    def test_prepare_forecast_positive_3(self):
        self.assertEqual(weather.prepare_forecast(get_weather({}))[0].keys(), dict_keys([30, 31, 1, 2, 3, 4]), "Wrong answer")


if __name__ == '__main__':
    unittest.main()
    