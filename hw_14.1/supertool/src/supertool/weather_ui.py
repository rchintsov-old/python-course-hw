import os
import sys
from contextlib import suppress

import numpy as np
import requests
from supertool import weather
from supertool import weather_qt
from PyQt5 import QtWidgets, QtGui, QtCore


TEST_MODE_STRING = \
"""App is running in the test mode.
You can see only the sample weather from Tawarano. 

For full access replace the OpenWeatherMap token \
placed in "{}"
with your own one and restart the app.

For testing just press "Get weather" button."""


class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()

        self.ui = weather_qt.Ui_MainWindow()
        self.ui.setupUi(self)

        self.label = self.ui.label

        self.forecasting = False
        self.order = []
        self.param_collection = {
            'temp': 'Temperature: {}°C',
            'descr': '{}',
            'hum': 'Humidity: {}%',
            'pres': 'Pressure: {} hPa',
            'cloud': 'Cloudiness: {}%',
            'wind': 'Wind speed: {} m/s',
        }
        
        self.filename = 'OpenWM token.txt'
        self.test_token = 'b6907d289e10d714a6e88b30761fae22'
        self.token = self.get_token()
        # check OWM token
        if self.token == self.test_token:
            self.test = True
            self.ui.line_city_widget.setText('Tawarano')
            self.label.setText(TEST_MODE_STRING.format(
                os.path.join(
                    *os.path.normpath(__file__).split(os.sep)[:-2] + \
                             ['static', self.filename])
            ))
        else:
            self.test = False
            self.label.setText('Please, type a city')

        # button connection
        self.ui.button_get.clicked.connect(self.get_weather)


    def get_token(self):
        """
        Gets a token if the file exists.
        Otherwise, creates a file with the test token.
        Suppress write errors if creates file.

        :return: token.
        :rtype: str
        """
        token = self.test_token
        path = os.path.join('..', 'static', self.filename)
        # if file exist
        if os.path.exists(path):
            with open(path, 'r') as f:
                line = f.readline().strip()
                token = line if line else token
        else: # if not exist - create it
            with suppress(Exception):
                with open(path, 'a') as f:
                    f.write(token)
        return token


    def get_info_from_widgets(self):
        """
        Getting info from widgets.

        :return: tuple with typed city, street and house number.
        :rtype: tuple
        """
        street, house = '', ''
        typed_city = self.ui.line_city_widget.text()
        extra_info = self.ui.street_house_line_w.text()
        # checks whether the street and house was specified
        if extra_info:
            try:
                street, house = [i.strip() for i in extra_info.split(',')]
            except ValueError:
                street = extra_info

        return typed_city, street, house


    def get_weather(self):
        """
        Geting info from user input, handle exceptions
        and return the weather data.
        """
        # getting user input
        city, street, house = self.get_info_from_widgets()

        # ad hoc solution for tabWidget objects: PyQt can't remove it
        # when once it was created.
        if self.forecasting:

            # filtering odd clicks
            if self.city == city and self.street == street and \
                self.house == house:
                # interruption
                return

            # remove all existing tabs if tabWidget already in use
            while self.tabWidget.count():
                self.tabWidget.removeTab(0)
        else:
            self.label.setText('Loading...')

        self.city, self.street, self.house = city, street, house

        # retrieving weather
        json_answer, failed = None, True
        try:
            coord_dict = weather.get_coordinates(city, street, house)
            json_answer = weather.get_weather(
                coord_dict, token=self.token, test=self.test)

        # possible exceptions, preparing user message
        except weather.AddressException as e_1:
            answer = e_1.args[0] + '\nPlease, type another one.' \
                if len(city) else 'The empty query. Type any address, please.'

        except weather.ConnecionFail as e_2:
            answer = e_2.args[0] + '\nTry again later.'

        except requests.exceptions.ConnectionError:
            answer = 'Connection failed.\n' \
                     'Check your Internet connection.'
        else:
            failed = False

        # shows error message to user
        if failed:
            if not self.forecasting:
                self.label.setText(answer)
            else:
                # creating tab with answer
                self.tabWidget.addTab(self.create_error_tab(answer), "")
                self.tabWidget.setTabText(0, 'Error')
                # func interruption
                return
        # prepare & show the weather
        if json_answer:
            weather_dict, current_day, city = weather.prepare_forecast(
                json_answer)
            self.label.setText('{} {}'.format(current_day, city))

            self.show_weather(weather_dict, current_day, city)
            # says that  tabWidget already appeared (in use)
            self.forecasting = True


    def create_error_tab(self, answer):
        """
        Creating tab object for further adding to tabWidget.

        :param str answer: error message to displaying.
        :return: tab object.
        :rtype: QObject
        """
        # creating tab
        error_tab = QtWidgets.QWidget()
        error_tab.setFont(self.ui.font)
        error_tab.setObjectName("err_tab")

        # add QLabel widget to tab
        label = QtWidgets.QLabel(error_tab)
        sizePolicy_e = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Maximum)
        sizePolicy_e.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy_e)
        label.setMinimumSize(QtCore.QSize(430, 260))
        label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        label.setFont(self.ui.font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setWordWrap(True)
        label.setMargin(5)
        label.setObjectName("err_label")

        # set error message to QLabel
        label.setText(answer)

        return error_tab


    def show_icon(self, parentLayout, icon, day):
        """
        Adds weather icon to specified layout.

        :param QObject parentLayout: parent layout.
        :param str icon: OpenWM icon code.
        :param int day: number for creating a unique objects signatures.
        :return: verticalWidget object (for joining with a general layout).
        :rtype: QObject
        """
        # path to static folder
        icon = os.path.join('..', 'static', 'img', icon + '.png')

        verticalWidget = QtWidgets.QWidget(parentLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.MinimumExpanding)
        verticalWidget.setSizePolicy(sizePolicy)
        verticalWidget.setMinimumSize(QtCore.QSize(50, 0))
        verticalWidget.setObjectName("verticalWidget{}".format(day))

        # yet another layout
        verticalLayout = QtWidgets.QVBoxLayout(verticalWidget)
        verticalLayout.setContentsMargins(0, 0, 18, 0)
        verticalLayout.setObjectName("verticalLayout{}".format(day))

        # create base object for Pixmap object (it's a label)
        label_Pixmap = QtWidgets.QLabel(verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        label_Pixmap.setSizePolicy(sizePolicy)
        label_Pixmap.setMinimumSize(QtCore.QSize(50, 50))
        label_Pixmap.setMaximumSize(QtCore.QSize(50, 50))
        label_Pixmap.setObjectName("Pixmap_base_{}".format(day))

        # add icon to label object
        pixmap = QtGui.QPixmap(icon)
        label_Pixmap.setPixmap(pixmap)
        # adding to layout
        verticalLayout.addWidget(label_Pixmap, 0, QtCore.Qt.AlignRight)
        # bottom spacer for it
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        # return object to adding to parent layout
        return verticalWidget


    def prepare_weather_dict(self, weather_dict, current_day):
        """
        Preparing weather to show.

        :param dict weather_dict: dict with weather.
        :param int current_day: current day.
        :return: prepared weather dict.
        :rtype: dict
        """
        output_dict = {}

        # current weather
        current = weather_dict.pop(current_day)
        self.order.append('Current')

        prepared = {
            'temp': round(current['temp'][0], 1)
                if current.get('temp') else None,
            'descr': current['description'][0].capitalize() + '.'
                if current.get('description') else 'no description',
            'hum': int(np.mean(current['humidity']))
                if current.get('humidity') else None,
            'pres': int(np.mean(current['pressure']))
                if current.get('pressure') else None,
            'cloud': int(np.mean(current['clouds']))
                if current.get('clouds') else None,
            'wind': round(np.mean(current['wind_speed']), 1) \
                if current.get('wind_speed') else None,
            'icon': current['icon'][-1][:-1]
                if current.get('icon') else None,
        }

        output_dict.update({self.order[-1]: prepared})

        # forecast
        for day in weather_dict:
            self.order.append(weather_dict[day]['date'])
            # transform description from several to one
            if weather_dict[day].get('description'):
                descriptions = weather_dict[day]['description']
                if len(set(descriptions)) > 1:
                    first_descr = descriptions[0]
                    while descriptions[-1] == first_descr:
                        descriptions.pop(-1)
                    last_descr = descriptions[-1]
                    description = 'From {} to {}.'.format(first_descr,
                                                         last_descr)
                else:
                    description = descriptions[0].capitalize() + '.'
            else:
                description = None

            # preparing parameters
            prepared_fc = {
                'descr': description,
                'hum': int(np.mean(weather_dict[day]['humidity'])) \
                    if weather_dict[day].get('humidity') else None,
                'pres': int(np.mean(weather_dict[day]['pressure'])) \
                    if weather_dict[day].get('pressure') else None,
                'cloud': int(np.mean(weather_dict[day]['clouds'])) \
                    if weather_dict[day].get('clouds') else None,
                'wind': round(np.mean(weather_dict[day]['wind_speed']), 1) \
                    if weather_dict[day].get('wind_speed') else None,
                'icon': weather_dict[day]['icon'][-1
                ][:-1] if weather_dict[day].get('icon') else None,
            }
            # adding temperature (min & max)
            if weather_dict[day].get('temp'):
                prepared_fc.update({
                    'temp': '{} - {}'.format(
                        round(min(weather_dict[day]['temp']), 1),
                        round(max(weather_dict[day]['temp']), 1),
                    )})

            output_dict.update({self.order[-1]: prepared_fc})

        return output_dict


    def show_weather(self, weather_dict, current_day, city):
        """
        The main showing function.
        Creates tabWidget object, tabs and other objects.

        :param dict weather_dict: dict with prepared weather.
        :param int current_day: current date.
        :param str city: city name (added for compatibility).
        :return: UI output.
        """
        prepared_weather_dict = self.prepare_weather_dict(
            weather_dict, current_day
        )

        if not self.forecasting:
            # create tab widget (for all tabs)
            self.tabWidget = QtWidgets.QTabWidget(self.ui.centralwidget)
            self.tabWidget.setObjectName("tabWidget")

        # creating weather tabs
        for day in self.order:

            current = prepared_weather_dict[day]
            # tab
            tab = QtWidgets.QWidget()
            tab.setFont(self.ui.font)
            tab.setObjectName("tab_{}".format(day))
            # grid in tab
            gridLayoutWidget = QtWidgets.QWidget(tab)
            gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 430, 260))
            gridLayoutWidget.setObjectName("gridLayoutWidget_{}".format(day))
            # left column for weather text
            gridLayout = QtWidgets.QGridLayout(gridLayoutWidget)
            gridLayout.setContentsMargins(10, 20, 5, 5)
            gridLayout.setObjectName("gridLayout_{}".format(day))

            # placing params
            row = 0
            for param in self.param_collection:
                if current.get(param) is not None:
                    param_w = QtWidgets.QLabel(gridLayoutWidget)
                    param_w.setObjectName(param + '_' + str(day))
                    param_w.setText(
                        self.param_collection[param].format(
                            current[param]))
                    gridLayout.addWidget(param_w, row, 0, 1, 1)
                    row += 1

            # bottom spacer for left column
            spacerItem = QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Expanding
            )
            gridLayout.addItem(spacerItem, row, 0, 1, 1)

            # get weather icon & construct right column for it
            if current.get('icon'):
                # self.show_icon - functon to constract the column
                gridLayout.addWidget(self.show_icon(
                    gridLayoutWidget, current['icon'], day), 0, 1, 4, 1)

            # add tab to tabWidget
            self.tabWidget.addTab(tab, "")

        # naming tabs by date
        for num, date in enumerate(self.order):
            self.tabWidget.setTabText(num, date)
        # set focus to first tab
        self.tabWidget.setCurrentIndex(0)

        # changing QLabel widget to tabWidget in main window
        # if tabWidget is not used yet
        # Note: reverse operation is not possible
        if not self.forecasting:
            self.ui.general_layout.replaceWidget(self.label, self.tabWidget)


def start():
    """The main function."""
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    start()

