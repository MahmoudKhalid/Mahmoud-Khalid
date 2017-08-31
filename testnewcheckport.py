# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test.ui'
#
# Created: Sun Jun 25 15:39:53 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(347, 506)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("program_defaults.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet(_fromUtf8("QWidget{\n"
"font: 75 10pt \"System\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QStatusBar\n"
"{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"    background-color: rgb(240, 240, 240);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 170, 0);\n"
"}\n"
""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 3)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 5px;\n"
"}"))
        self.pushButton_4.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("maximize-window-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 5px;\n"
"}"))
        self.pushButton_6.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 5px;\n"
"}"))
        self.pushButton_5.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_2.addWidget(self.radioButton, 3, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_2.addWidget(self.radioButton_2, 4, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 4, 1, 1, 2)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget, 5, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"border: 2px solid transpent;\n"
"border-radius: 6px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    border-color: rgb(0, 255, 0);\n"
"}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 6, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{\n"
"border: 2px solid transpent;\n"
"border-radius: 6px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    border-color: rgb(0, 255, 0);\n"
"}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{\n"
"border: 2px solid transpent;\n"
"border-radius: 6px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    border-color: rgb(0, 255, 0);\n"
"}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 19))
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setStatusTip(_fromUtf8(""))
        self.menuFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuFile.setAutoFillBackground(False)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setCheckable(False)
        self.actionOpen_File.setIcon(icon3)
        self.actionOpen_File.setWhatsThis(_fromUtf8(""))
        self.actionOpen_File.setVisible(True)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHow_to_work = QtGui.QAction(MainWindow)
        self.actionHow_to_work.setObjectName(_fromUtf8("actionHow_to_work"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionMaximize = QtGui.QAction(MainWindow)
        self.actionMaximize.setIcon(icon1)
        self.actionMaximize.setObjectName(_fromUtf8("actionMaximize"))
        self.menuFile.addAction(self.actionRun)
        self.menuFile.addAction(self.actionStop)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionMaximize)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHow_to_work)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidget.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_3.setDisabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_2.setDisabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_4.setDisabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_3.setEnabled)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_2.setEnabled)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_4.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Check Port Network", None))
        self.lineEdit.setToolTip(_translate("MainWindow", "URL", None))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Enter Website / URL / IP Adreass", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Ex : https://www.google.com", None))
        self.progressBar.setToolTip(_translate("MainWindow", "Loading...", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Maximize Screen", None))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Clear dateils", None))
        self.pushButton_5.setToolTip(_translate("MainWindow", "Save Dateils", None))
        self.radioButton.setToolTip(_translate("MainWindow", "Select more of port", None))
        self.radioButton.setStatusTip(_translate("MainWindow", "Select more of port", None))
        self.radioButton.setText(_translate("MainWindow", "Select more of port", None))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "Start Port", None))
        self.lineEdit_2.setStatusTip(_translate("MainWindow", "Start Port", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "From", None))
        self.lineEdit_4.setToolTip(_translate("MainWindow", "End port", None))
        self.lineEdit_4.setStatusTip(_translate("MainWindow", "End port", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "To", None))
        self.radioButton_2.setStatusTip(_translate("MainWindow", "Select one port", None))
        self.radioButton_2.setWhatsThis(_translate("MainWindow", "Select one port", None))
        self.radioButton_2.setText(_translate("MainWindow", "Select one port", None))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "Port Number ??", None))
        self.lineEdit_3.setStatusTip(_translate("MainWindow", "Port Number ??", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Port", None))
        self.listWidget.setStatusTip(_translate("MainWindow", "Runing...", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Run Now...", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setToolTip(_translate("MainWindow", "Run", None))
        self.pushButton.setText(_translate("MainWindow", "Run", None))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Stop", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Exit", None))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Save Dateils", None))
        self.actionOpen_File.setStatusTip(_translate("MainWindow", "Select file to save", None))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "about program", None))
        self.actionHow_to_work.setText(_translate("MainWindow", "How to work", None))
        self.actionHow_to_work.setStatusTip(_translate("MainWindow", "view more to how to work", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionRun.setStatusTip(_translate("MainWindow", "Run", None))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionStop.setStatusTip(_translate("MainWindow", "Stop", None))
        self.actionStop.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionClear.setText(_translate("MainWindow", "Clear", None))
        self.actionClear.setStatusTip(_translate("MainWindow", "Clear dateils", None))
        self.actionClear.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize", None))
        self.actionMaximize.setStatusTip(_translate("MainWindow", "Maximize Screen", None))

#import photos_rc
