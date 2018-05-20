from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.select_fold_butt = QtWidgets.QPushButton(self.centralwidget)
        self.select_fold_butt.setMinimumSize(QtCore.QSize(100, 0))
        self.select_fold_butt.setDefault(True)
        self.select_fold_butt.setObjectName("select_fold_butt")
        self.gridLayout.addWidget(self.select_fold_butt, 9, 2, 1, 1)

        self.analyse_butt = QtWidgets.QPushButton(self.centralwidget)
        self.analyse_butt.setMinimumSize(QtCore.QSize(80, 0))
        self.analyse_butt.setObjectName("analyse_butt")
        self.gridLayout.addWidget(self.analyse_butt, 9, 3, 1, 1)

        self.fold_sel_line_editor = QtWidgets.QLineEdit(self.centralwidget)
        self.fold_sel_line_editor.setText("")
        self.fold_sel_line_editor.setClearButtonEnabled(False)
        self.fold_sel_line_editor.setObjectName("fold_sel_line_editor")
        self.gridLayout.addWidget(self.fold_sel_line_editor, 9, 1, 1, 1)
        # self.fold_sel_line_editor.text

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setAcceptDrops(False)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.treeWidget.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.treeWidget.setAutoExpandDelay(0)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")

        self.treeWidget.header().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.treeWidget, 13, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Similar files"))
        self.select_fold_butt.setText(_translate("MainWindow", "Select folder"))
        self.analyse_butt.setText(_translate("MainWindow", "Analyse"))
        self.fold_sel_line_editor.setPlaceholderText(_translate("MainWindow", "Select folder or type path here"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Duplicates"))

