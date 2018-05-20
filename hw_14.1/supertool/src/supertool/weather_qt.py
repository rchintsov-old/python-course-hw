from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(450, 300))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)

        # font size
        font = QtGui.QFont()
        font.setPointSize(11)
        self.font = font

        # window title
        MainWindow.setWindowTitle("Weather")

        # central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        # general layout
        self.general_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.general_layout.setObjectName("general_layout")

        # ------------ header -------------------------------------
        # layout for line w & pushButton-
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.line_city_widget = QtWidgets.QLineEdit(self.centralwidget)
        self.line_city_widget.setObjectName("line_city_widget")
        self.line_city_widget.setFont(font)
        self.line_city_widget.setPlaceholderText("City")
        self.horizontalLayout.addWidget(self.line_city_widget)

        self.button_get = QtWidgets.QPushButton(self.centralwidget)
        self.button_get.setObjectName("button_get")
        self.button_get.setFont(font)
        self.button_get.setMinimumWidth(125)
        self.button_get.setText("Get weather")
        self.horizontalLayout.addWidget(self.button_get)

        self.general_layout.addLayout(self.horizontalLayout)
        # end layout

        # street & house w
        self.street_house_line_w = QtWidgets.QLineEdit(self.centralwidget)
        self.street_house_line_w.setObjectName("street_house_line_w")
        self.street_house_line_w.setFont(font)
        self.street_house_line_w.setPlaceholderText(
            "Street, house number (optional, separated by comma)"
        )
        self.general_layout.addWidget(self.street_house_line_w)
        # ----------------------------------------------------------

        # start label
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setFont(self.font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(5)
        self.label.setObjectName("label")

        self.general_layout.addWidget(self.label)


        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
