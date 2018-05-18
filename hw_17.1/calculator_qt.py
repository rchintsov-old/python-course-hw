from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 664)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setGeometry(QtCore.QRect(100, 60, 551, 111))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lcd.setFont(font)
        self.lcd.setToolTipDuration(-1)
        self.lcd.setDigitCount(9)
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd.setProperty("value", 0.0)
        self.lcd.setProperty("intValue", 0)
        self.lcd.setObjectName("lcd")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 190, 411, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_digits = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_digits.setContentsMargins(0, 0, 0, 0)
        self.grid_digits.setObjectName("grid_digits")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(550, 190, 101, 401))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.grid_operations = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_operations.setContentsMargins(0, 0, 0, 0)
        self.grid_operations.setObjectName("grid_operations")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))

