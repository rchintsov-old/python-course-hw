import functools
import sys

import calculator_qt
from PyQt5 import QtGui, QtWidgets


class MainApplication(QtWidgets.QMainWindow):
    """Main application class"""
    def __init__(self):
        super(MainApplication, self).__init__()

        self.ui = calculator_qt.Ui_MainWindow()
        self.ui.setupUi(self)
        self.expression = ''
        self.collector = ''
        self.just_evaluated = False
        self.dot_allowed = True

        # calculator actions
        self.actions_ = {
            '+': '+',
            '-': '-',
            '/': '/',
            '*': '*',
            '^': '**',
            '=': '',
        }
        # numpad keys
        self.numpad = {
            '1': (1, 1),
            '2': (1, 2),
            '3': (1, 3),
            '4': (2, 1),
            '5': (2, 2),
            '6': (2, 3),
            '7': (3, 1),
            '8': (3, 2),
            '9': (3, 3),
            '.': (4, 1),
            '0': (4, 2),
            'AC': (4, 3),
        }

        # buiding keys
        for key in self.numpad:
            row = self.numpad[key][0]
            col = self.numpad[key][1]

            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName("button{}".format(key))
            self.ui.grid_digits.addWidget(button, row, col, 1, 1)
            button.setText(key)

            button.clicked.connect(functools.partial(self.button_pressed, key))

        # keys for actions
        for num, action in enumerate(self.actions_):

            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName("button{}".format(action))
            self.ui.grid_operations.addWidget(button, num, 0, 1, 1)
            button.setText(action)

            button.clicked.connect(functools.partial(self.button_action_add, action))


    def button_pressed(self, key):
        """
        Handling numeric & AC key pressing.

        :param str key: key that pressed.
        :return: changes several self objects.
        """
        if key == 'AC':
            self.expression = ''
            self.collector = ''
            self.dot_allowed = True
            self.just_evaluated = False
            self.ui.lcd.display(0)
        elif key == '.':
            if self.dot_allowed:
                self.collector += key
                self.ui.lcd.display(self.collector)
                self.dot_allowed = False
        else:
            if not self.just_evaluated:
                self.collector += key
            self.ui.lcd.display(self.collector)


    def button_action_add(self, action):
        """
        Handling action keys pressing.

        :param str action: action.
        :return: changes several self objects.
        :exception ZeroDivisionError: suppress it and return 0.
        """
        if action in ['+', '-', '/', '*', '^']:
            self.expression += self.collector
            self.just_evaluated = False
            self.expression += self.actions_[action]
            self.ui.lcd.display(self.collector)
            self.dot_allowed = True
            self.collector = ''

        elif action == '=':
            if not self.just_evaluated:
                self.expression += self.collector
                try:
                    print('prop')
                    result = eval(self.expression)
                except ZeroDivisionError:
                    result = 0
                if result:
                    if int(result):
                        self.expression = str(int(result))[:10] if result % \
                            int(result) == 0 else str(result)[:10]
                    else:
                        self.expression = str(result)[:10]
                else:
                    self.expression = str(0)
                self.collector = self.expression
                self.expression = ''
                self.ui.lcd.display(self.collector)
                self.just_evaluated = True
                self.dot_allowed = False


app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()
sys.exit(app.exec_())
