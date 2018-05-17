import io
import unittest
from contextlib import redirect_stdout

from supertool import weather


class TestGetCoordinates(unittest.TestCase):

    def test_get_coordinates_positive(self):
        self.assertEqual(weather.get_coordinates('Санкт-Петербург'),
                         {'lat': '59.938732', 'lon': '30.316229'}, "Wrong answer")

    # testing an exception SystemExit: 2
    def test_get_coordinates_with_Exit_2_exception(self):

        with self.assertRaises(SystemExit) as e:
            weather.get_coordinates('лытдыбр')

        self.assertEqual(e.exception.args[0], 2, "Exit code doesn't match")


class TestGetWeather(unittest.TestCase):

    def test_get_weather_positive(self):
        self.assertEqual(list(weather.get_weather({'lat': '59.938732', 'lon': '30.316229'}).keys()),
                         ['cod', 'message', 'cnt', 'list', 'city'], "Wrong answer")


class TestPrepareForecast(unittest.TestCase):

    def test_prepare_forecast_positive(self):
        self.assertEqual(weather.prepare_forecast(weather.get_weather({}))[2],
                         'Tawarano', "Wrong answer")


    def test_prepare_forecast_positive_2(self):
        self.assertEqual(weather.prepare_forecast(weather.get_weather({}))[1], 30,
                         "Wrong answer")


    def test_prepare_forecast_positive_3(self):
        self.assertEqual(list(weather.prepare_forecast(weather.get_weather({}))[0].keys()),
                         [30, 31, 1, 2, 3, 4], "Wrong answer")


class TestPrintWeather(unittest.TestCase):

    # testing stdout
    def test_print_weather_with_stdout_redirect(self):

        expected_stdout = '\n-- Weather in Tawarano --\n\n' \
                          'Current:\n\n10.6°C, clear sky\nHumidity: 100%' \
                          '\nPressure: 1017 hPa\nCloudiness: 0%\n' \
                          'Wind speed: 7.3 m/s\n'

        handler = io.StringIO()

        with redirect_stdout(handler):
            result = weather.print_weather(
                *weather.prepare_forecast(
                    weather.get_weather({})
                ))

        self.assertEqual(handler.getvalue()[:125], expected_stdout, 'Wrong stdout')


if __name__ == '__main__':
    unittest.main()
