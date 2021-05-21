from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import math
import cmath
from locale import lang


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(400, 475)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 400, 450))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.Tabs.setFont(font)
        self.Tabs.setObjectName("Tabs")
        self.arifm = QtWidgets.QWidget()
        self.arifm.setObjectName("arifm")
        self.btn_6 = QtWidgets.QPushButton(self.arifm)
        self.btn_6.setGeometry(QtCore.QRect(260, 210, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_6.setObjectName("btn_6")
        self.btn_4 = QtWidgets.QPushButton(self.arifm)
        self.btn_4.setGeometry(QtCore.QRect(0, 210, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.arifm)
        self.btn_5.setGeometry(QtCore.QRect(130, 210, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_5.setObjectName("btn_5")
        self.btn_9 = QtWidgets.QPushButton(self.arifm)
        self.btn_9.setGeometry(QtCore.QRect(260, 280, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_9.setFont(font)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_9.setObjectName("btn_9")
        self.btn_3 = QtWidgets.QPushButton(self.arifm)
        self.btn_3.setGeometry(QtCore.QRect(260, 140, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_3.setObjectName("btn_3")
        self.btn_7 = QtWidgets.QPushButton(self.arifm)
        self.btn_7.setGeometry(QtCore.QRect(0, 280, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_7.setObjectName("btn_7")
        self.btn_result = QtWidgets.QPushButton(self.arifm)
        self.btn_result.setGeometry(QtCore.QRect(260, 350, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.btn_result.setFont(font)
        self.btn_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_result.setStyleSheet("color: rgb(231, 231, 231);\n"
"background-color: rgb(3, 83, 255);")
        self.btn_result.setObjectName("btn_result")
        self.btn_2 = QtWidgets.QPushButton(self.arifm)
        self.btn_2.setGeometry(QtCore.QRect(130, 140, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_2.setObjectName("btn_2")
        self.btn_0 = QtWidgets.QPushButton(self.arifm)
        self.btn_0.setGeometry(QtCore.QRect(130, 350, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_0.setFont(font)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_0.setObjectName("btn_0")
        self.btn_1 = QtWidgets.QPushButton(self.arifm)
        self.btn_1.setGeometry(QtCore.QRect(0, 140, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.btn_8 = QtWidgets.QPushButton(self.arifm)
        self.btn_8.setGeometry(QtCore.QRect(130, 280, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_8.setObjectName("btn_8")
        self.label_result1 = QtWidgets.QLabel(self.arifm)
        self.label_result1.setGeometry(QtCore.QRect(0, 5, 390, 60))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.label_result1.setFont(font)
        self.label_result1.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.label_result1.setObjectName("label_result1")
        self.btn_point = QtWidgets.QPushButton(self.arifm)
        self.btn_point.setGeometry(QtCore.QRect(0, 350, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_point.setFont(font)
        self.btn_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_point.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_point.setObjectName("btn_point")
        self.btn_clear_all = QtWidgets.QPushButton(self.arifm)
        self.btn_clear_all.setGeometry(QtCore.QRect(0, 70, 195, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_clear_all.setFont(font)
        self.btn_clear_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_all.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.btn_clear_el = QtWidgets.QPushButton(self.arifm)
        self.btn_clear_el.setGeometry(QtCore.QRect(195, 70, 195, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_clear_el.setFont(font)
        self.btn_clear_el.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_el.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_clear_el.setObjectName("btn_clear_el")
        self.Tabs.addTab(self.arifm, "")
        self.complex = QtWidgets.QWidget()
        self.complex.setObjectName("complex")
        self.btn_c_6 = QtWidgets.QPushButton(self.complex)
        self.btn_c_6.setGeometry(QtCore.QRect(260, 300, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_6.setFont(font)
        self.btn_c_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_6.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_6.setObjectName("btn_c_6")
        self.btn_c_2 = QtWidgets.QPushButton(self.complex)
        self.btn_c_2.setGeometry(QtCore.QRect(130, 260, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_2.setFont(font)
        self.btn_c_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_2.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_2.setObjectName("btn_c_2")
        self.ladel_c_res1 = QtWidgets.QLabel(self.complex)
        self.ladel_c_res1.setGeometry(QtCore.QRect(0, 120, 390, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.ladel_c_res1.setFont(font)
        self.ladel_c_res1.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.ladel_c_res1.setObjectName("ladel_c_res1")
        self.btn_c_1 = QtWidgets.QPushButton(self.complex)
        self.btn_c_1.setGeometry(QtCore.QRect(0, 260, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_1.setFont(font)
        self.btn_c_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_1.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_c_1.setObjectName("btn_c_1")
        self.btn_c_4 = QtWidgets.QPushButton(self.complex)
        self.btn_c_4.setGeometry(QtCore.QRect(0, 300, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_4.setFont(font)
        self.btn_c_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_4.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_4.setObjectName("btn_c_4")
        self.btn_c_7 = QtWidgets.QPushButton(self.complex)
        self.btn_c_7.setGeometry(QtCore.QRect(0, 340, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_7.setFont(font)
        self.btn_c_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_7.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_7.setObjectName("btn_c_7")
        self.btn_c_result = QtWidgets.QPushButton(self.complex)
        self.btn_c_result.setGeometry(QtCore.QRect(260, 380, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.btn_c_result.setFont(font)
        self.btn_c_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_result.setStyleSheet("color: rgb(231, 231, 231);\n"
"background-color: rgb(3, 83, 255);")
        self.btn_c_result.setObjectName("btn_c_result")
        self.btn_c_5 = QtWidgets.QPushButton(self.complex)
        self.btn_c_5.setGeometry(QtCore.QRect(130, 300, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_5.setFont(font)
        self.btn_c_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_5.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_5.setObjectName("btn_c_5")
        self.btn_c_8 = QtWidgets.QPushButton(self.complex)
        self.btn_c_8.setGeometry(QtCore.QRect(130, 340, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_8.setFont(font)
        self.btn_c_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_8.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_8.setObjectName("btn_c_8")
        self.btn_c_3 = QtWidgets.QPushButton(self.complex)
        self.btn_c_3.setGeometry(QtCore.QRect(260, 260, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_3.setFont(font)
        self.btn_c_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_3.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_3.setObjectName("btn_c_3")
        self.btn_c_9 = QtWidgets.QPushButton(self.complex)
        self.btn_c_9.setGeometry(QtCore.QRect(260, 340, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_9.setFont(font)
        self.btn_c_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_9.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_9.setObjectName("btn_c_9")
        self.btn_c_0 = QtWidgets.QPushButton(self.complex)
        self.btn_c_0.setGeometry(QtCore.QRect(130, 380, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_0.setFont(font)
        self.btn_c_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_0.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);")
        self.btn_c_0.setObjectName("btn_c_0")
        self.btn_c_point = QtWidgets.QPushButton(self.complex)
        self.btn_c_point.setGeometry(QtCore.QRect(0, 380, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_point.setFont(font)
        self.btn_c_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_point.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_c_point.setObjectName("btn_c_point")
        self.lab_real = QtWidgets.QLabel(self.complex)
        self.lab_real.setGeometry(QtCore.QRect(0, 70, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.lab_real.setFont(font)
        self.lab_real.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.lab_real.setObjectName("lab_real")
        self.lab_imaginary = QtWidgets.QLabel(self.complex)
        self.lab_imaginary.setGeometry(QtCore.QRect(199, 70, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.lab_imaginary.setFont(font)
        self.lab_imaginary.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.lab_imaginary.setObjectName("lab_imaginary")
        self.rB_real = QtWidgets.QRadioButton(self.complex)
        self.rB_real.setGeometry(QtCore.QRect(10, 10, 170, 60))
        self.rB_real.setObjectName("rB_real")
        self.rB_im = QtWidgets.QRadioButton(self.complex)
        self.rB_im.setGeometry(QtCore.QRect(200, 10, 160, 60))
        self.rB_im.setObjectName("rB_im")
        self.btn_c_minus = QtWidgets.QPushButton(self.complex)
        self.btn_c_minus.setGeometry(QtCore.QRect(130, 220, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_minus.setFont(font)
        self.btn_c_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_minus.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_c_minus.setObjectName("btn_c_minus")
        self.btn_c_clear = QtWidgets.QPushButton(self.complex)
        self.btn_c_clear.setGeometry(QtCore.QRect(260, 220, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_clear.setFont(font)
        self.btn_c_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_clear.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_c_clear.setObjectName("btn_c_clear")
        self.label_pl = QtWidgets.QLabel(self.complex)
        self.label_pl.setGeometry(QtCore.QRect(167, 75, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.label_pl.setFont(font)
        self.label_pl.setStyleSheet("")
        self.label_pl.setObjectName("label_pl")
        self.label_i = QtWidgets.QLabel(self.complex)
        self.label_i.setGeometry(QtCore.QRect(355, 70, 30, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.label_i.setFont(font)
        self.label_i.setStyleSheet("")
        self.label_i.setObjectName("label_i")
        self.ladel_c_res2 = QtWidgets.QLabel(self.complex)
        self.ladel_c_res2.setGeometry(QtCore.QRect(0, 170, 390, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.ladel_c_res2.setFont(font)
        self.ladel_c_res2.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.ladel_c_res2.setObjectName("ladel_c_res2")
        self.btn_c_clear_all = QtWidgets.QPushButton(self.complex)
        self.btn_c_clear_all.setGeometry(QtCore.QRect(0, 220, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.btn_c_clear_all.setFont(font)
        self.btn_c_clear_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_c_clear_all.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(231, 231, 231);\n"
"")
        self.btn_c_clear_all.setObjectName("btn_c_clear_all")
        self.Tabs.addTab(self.complex, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.lang = QtWidgets.QMenu(self.menu)
        self.lang.setObjectName("lang")
        self.help = QtWidgets.QMenu(self.menu)
        self.help.setObjectName("help")
        mainWindow.setMenuBar(self.menubar)
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(mainWindow)
        self.action_3.setObjectName("action_3")
        self.rus = QtWidgets.QAction(mainWindow)
        self.rus.setCheckable(True)
        self.rus.setChecked(True)
        self.rus.setObjectName("rus")
        self.en = QtWidgets.QAction(mainWindow)
        self.en.setCheckable(True)
        self.en.setObjectName("en")
        self.action_8 = QtWidgets.QAction(mainWindow)
        self.action_8.setObjectName("action_8")
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.ref = QtWidgets.QAction(mainWindow)
        self.ref.setObjectName("ref")
        self.forum = QtWidgets.QAction(mainWindow)
        self.forum.setObjectName("forum")
        self.about = QtWidgets.QAction(mainWindow)
        self.about.setObjectName("about")
        self.action_10 = QtWidgets.QAction(mainWindow)
        self.action_10.setObjectName("action_10")
        self.mExit = QtWidgets.QAction(mainWindow)
        self.mExit.setObjectName("mExit")
        self.lang.addSeparator()
        self.lang.addAction(self.rus)
        self.lang.addAction(self.en)
        self.help.addAction(self.ref)
        self.help.addAction(self.forum)
        self.menu.addAction(self.lang.menuAction())
        self.menu.addAction(self.help.menuAction())
        self.menu.addAction(self.about)
        self.menu.addSeparator()
        self.menu.addAction(self.mExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        self.btn_click()
        self.rB_real.toggled.connect(self.rbtn_click_r)
        self.rB_im.toggled.connect(self.rbtn_click_i)
        self.btn_c_result.clicked.connect(self.result_c)
        self.btn_c_clear_all.clicked.connect(lambda: self.write_num_im(self.btn_c_clear_all.text()))

        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Sqrt root"))
        self.btn_6.setText(_translate("mainWindow", "6"))
        self.btn_4.setText(_translate("mainWindow", "4"))
        self.btn_5.setText(_translate("mainWindow", "5"))
        self.btn_9.setText(_translate("mainWindow", "9"))
        self.btn_3.setText(_translate("mainWindow", "3"))
        self.btn_7.setText(_translate("mainWindow", "7"))
        self.btn_result.setText(_translate("mainWindow", "="))
        self.btn_2.setText(_translate("mainWindow", "2"))
        self.btn_0.setText(_translate("mainWindow", "0"))
        self.btn_1.setText(_translate("mainWindow", "1"))
        self.btn_8.setText(_translate("mainWindow", "8"))
        self.label_result1.setText(_translate("mainWindow", "0"))
        self.btn_point.setText(_translate("mainWindow", "."))
        self.btn_clear_all.setText(_translate("mainWindow", "CE"))
        self.btn_clear_el.setText(_translate("mainWindow", "C"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.arifm), _translate("mainWindow", "Арифметические"))
        self.btn_c_6.setText(_translate("mainWindow", "6"))
        self.btn_c_2.setText(_translate("mainWindow", "2"))
        self.ladel_c_res1.setText(_translate("mainWindow", "Первый корень:"))
        self.btn_c_1.setText(_translate("mainWindow", "1"))
        self.btn_c_4.setText(_translate("mainWindow", "4"))
        self.btn_c_7.setText(_translate("mainWindow", "7"))
        self.btn_c_result.setText(_translate("mainWindow", "="))
        self.btn_c_5.setText(_translate("mainWindow", "5"))
        self.btn_c_8.setText(_translate("mainWindow", "8"))
        self.btn_c_3.setText(_translate("mainWindow", "3"))
        self.btn_c_9.setText(_translate("mainWindow", "9"))
        self.btn_c_0.setText(_translate("mainWindow", "0"))
        self.btn_c_point.setText(_translate("mainWindow", "."))
        self.lab_real.setText(_translate("mainWindow", "0"))
        self.lab_imaginary.setText(_translate("mainWindow", "0"))
        self.rB_real.setText(_translate("mainWindow", "Вводить \n"
"действительную\n"
"часть"))
        self.rB_im.setText(_translate("mainWindow", "Вводить \n"
"мнимую\n"
"часть"))
        self.btn_c_minus.setText(_translate("mainWindow", "-"))
        self.btn_c_clear.setText(_translate("mainWindow", "C"))
        self.label_pl.setText(_translate("mainWindow", "+"))
        self.label_i.setText(_translate("mainWindow", "* i "))
        self.ladel_c_res2.setText(_translate("mainWindow", "Второй корень:"))
        self.btn_c_clear_all.setText(_translate("mainWindow", "CE"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.complex), _translate("mainWindow", "Комплексные"))
        self.menu.setTitle(_translate("mainWindow", "Меню"))
        self.lang.setTitle(_translate("mainWindow", "Язык"))
        self.help.setTitle(_translate("mainWindow", "Помощь"))
        self.action_2.setText(_translate("mainWindow", "Целые"))
        self.action_3.setText(_translate("mainWindow", "Справка"))
        self.rus.setText(_translate("mainWindow", "Русский"))
        self.en.setText(_translate("mainWindow", "English"))
        self.action_8.setText(_translate("mainWindow", "Комплексные"))
        self.action.setText(_translate("mainWindow", "О программе"))
        self.ref.setText(_translate("mainWindow", "Справка"))
        self.forum.setText(_translate("mainWindow", "Форум поддержки"))
        self.about.setText(_translate("mainWindow", "О программе"))
        self.action_10.setText(_translate("mainWindow", "Выход"))
        self.mExit.setText(_translate("mainWindow", "Выход"))

    def result_c(self):
        if self.ladel_c_res1.text().find("=") == -1:
                a = float(self.lab_real.text())
                b = float(self.lab_imaginary.text())
                c = complex(str(a) + "+" + str(b) + "j")
                if b == 0:
                    self.ladel_c_res1.setText("=Число не комплексное; для его вычис-")
                    self.ladel_c_res2.setText("ления перейдите на другой калькулятор")
                elif a != 0:
                    r = math.sqrt(a * a + b * b)
                    f = math.atan(b / a)
                    cos = math.cos(f / 2.0)
                    sin = math.sin(f / 2.0)
                    cos2 = math.cos((f + 2 * 3.14) / 2)
                    sin2 = math.sin((f + 2 * 3.14) / 2)
                    res1 = str(round(math.sqrt(r) * cos, 2)) + " + (" + str(round(math.sqrt(r) * sin, 2)) + ") * i"
                    res2 = str(round(math.sqrt(r) * cos2, 2)) + " + (" + str(round(math.sqrt(r) * sin2, 2)) + ") * i"
                    self.ladel_c_res1.setText(self.ladel_c_res1.text() + " =" + res1)
                    self.ladel_c_res2.setText(self.ladel_c_res2.text() + " =" + res2)
                else:
                    res = cmath.sqrt(c)
                    self.ladel_c_res1.setText(self.ladel_c_res1.text() + " =" + str(round(res.real, 2) + round(res.imag,2) * 1j))
                    self.ladel_c_res2.setText("=Второго корня в данной ситуации нет")


    def rbtn_click_r(self):
        if self.rB_real.isSignalConnected:
            self.rB_real.disconnect()
            self.rB_real.toggled.connect(self.rbtn_click_r)
            self.disconn()
            self.btn_c_0.clicked.connect(lambda: self.write_num_real(self.btn_c_0.text()))
            self.btn_c_1.clicked.connect(lambda: self.write_num_real(self.btn_c_1.text()))
            self.btn_c_2.clicked.connect(lambda: self.write_num_real(self.btn_c_2.text()))
            self.btn_c_3.clicked.connect(lambda: self.write_num_real(self.btn_c_3.text()))
            self.btn_c_4.clicked.connect(lambda: self.write_num_real(self.btn_c_4.text()))
            self.btn_c_5.clicked.connect(lambda: self.write_num_real(self.btn_c_5.text()))
            self.btn_c_6.clicked.connect(lambda: self.write_num_real(self.btn_c_6.text()))
            self.btn_c_7.clicked.connect(lambda: self.write_num_real(self.btn_c_7.text()))
            self.btn_c_8.clicked.connect(lambda: self.write_num_real(self.btn_c_8.text()))
            self.btn_c_9.clicked.connect(lambda: self.write_num_real(self.btn_c_9.text()))
            self.btn_c_point.clicked.connect(lambda: self.write_num_real(self.btn_c_point.text()))
            self.btn_c_clear.clicked.connect(lambda: self.write_num_real(self.btn_c_clear.text()))
            self.btn_c_minus.clicked.connect(lambda: self.write_num_real(self.btn_c_minus.text()))

    def rbtn_click_i(self):
        if self.rB_im.isSignalConnected:
            self.rB_im.disconnect()
            self.rB_im.toggled.connect(self.rbtn_click_i)
            self.disconn()
            self.btn_c_0.clicked.connect(lambda: self.write_num_im(self.btn_c_0.text()))
            self.btn_c_1.clicked.connect(lambda: self.write_num_im(self.btn_c_1.text()))
            self.btn_c_2.clicked.connect(lambda: self.write_num_im(self.btn_c_2.text()))
            self.btn_c_3.clicked.connect(lambda: self.write_num_im(self.btn_c_3.text()))
            self.btn_c_4.clicked.connect(lambda: self.write_num_im(self.btn_c_4.text()))
            self.btn_c_5.clicked.connect(lambda: self.write_num_im(self.btn_c_5.text()))
            self.btn_c_6.clicked.connect(lambda: self.write_num_im(self.btn_c_6.text()))
            self.btn_c_7.clicked.connect(lambda: self.write_num_im(self.btn_c_7.text()))
            self.btn_c_8.clicked.connect(lambda: self.write_num_im(self.btn_c_8.text()))
            self.btn_c_9.clicked.connect(lambda: self.write_num_im(self.btn_c_9.text()))
            self.btn_c_point.clicked.connect(lambda: self.write_num_im(self.btn_c_point.text()))
            self.btn_c_clear.clicked.connect(lambda: self.write_num_im(self.btn_c_clear.text()))
            self.btn_c_minus.clicked.connect(lambda: self.write_num_im(self.btn_c_minus.text()))

    def clear_res(self):
        if self.ladel_c_res1.text().find("=") != -1:
            self.ladel_c_res1.setText("Первый корень:")
            self.ladel_c_res2.setText("Второй корень:")

    def write_num_real(self, num):
        self.clear_res()
        if num == 'C' and self.lab_real.text().find("=") == -1:
            if len(self.lab_real.text()) == 1:
                self.lab_real.setText("0")
            else:
                self.lab_real.setText(self.lab_real.text()[:-1])
        elif num == 'C' and self.lab_real.text().find("=") != -1:
            self.lab_real.setText("0")
        elif num == 'CE':
            self.lab_real.setText("0")
            self.lab_imaginary.setText("0")
        elif self.lab_real.text() == '0':
            self.lab_real.setText(num)
        else:
            if len(self.lab_real.text()) < 10:
                if  num == '.' and self.lab_real.text().find('.') != -1:
                    self.lab_real.setText(self.lab_real.text())
                elif num == '-' and (self.lab_real.text() != '0'):
                    self.lab_real.setText(self.lab_real.text())
                else:
                    self.lab_real.setText(self.lab_real.text() + num)



    def write_num_im(self, num):
        self.clear_res()
        if num == 'C' and self.lab_imaginary.text().find("=") == -1:
            if len(self.lab_imaginary.text()) == 1:
                self.lab_imaginary.setText("0")
            else:
                self.lab_imaginary.setText(self.lab_imaginary.text()[:-1])
        elif num == 'C' and self.lab_imaginary.text().find("=") != -1:
            self.lab_imaginary.setText("0")
        elif num == 'CE':
            self.lab_real.setText("0")
            self.lab_imaginary.setText("0")
        elif self.lab_imaginary.text() == '0':
            self.lab_imaginary.setText(num)
        else:
            if len(self.lab_imaginary.text()) < 10:
                if  num == '.' and self.lab_imaginary.text().find('.') != -1:
                    self.lab_imaginary.setText(self.lab_imaginary.text())
                elif num == '-' and (self.lab_imaginary.text() != '0'):
                    self.lab_imaginary.setText(self.lab_imaginary.text())
                else:
                    self.lab_imaginary.setText(self.lab_imaginary.text() + num)

    def btn_click(self):
        self.btn_0.clicked.connect(lambda: self.write_num1(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_num1(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_num1(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_num1(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_num1(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_num1(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_num1(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_num1(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_num1(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_num1(self.btn_9.text()))
        self.btn_point.clicked.connect(lambda: self.write_num1(self.btn_point.text()))
        self.btn_clear_el.clicked.connect(lambda: self.write_num1(self.btn_clear_el.text()))
        self.btn_clear_all.clicked.connect(lambda: self.write_num1(self.btn_clear_all.text()))
        self.btn_result.clicked.connect(self.result1)

    def result1(self):
        if self.label_result1.text().find("=") == -1:
            self.label_result1.setText("= " + str(round(math.sqrt(float(self.label_result1.text())), 2)))

    def write_num1(self, num):
        if num == 'C' and self.label_result1.text().find("=") == -1:
            if len(self.label_result1.text()) == 1:
                self.label_result1.setText("0")
            else:
                self.label_result1.setText(self.label_result1.text()[:-1])
        elif num == 'C' and self.label_result1.text().find("=") != -1:
            self.label_result1.setText("0")
        elif num == 'CE':
            self.label_result1.setText("0")
        elif self.label_result1.text() == '0' or self.label_result1.text().find("=") != -1:
            self.label_result1.setText(num)
        else:
            if len(self.label_result1.text()) < 10:
                if num == '.' and self.label_result1.text().find('.') != -1:
                    self.label_result1.setText(self.label_result1.text())
                else:
                    self.label_result1.setText(self.label_result1.text() + num)

    def disconn(self):
        if self.btn_c_0.isSignalConnected:
            self.btn_c_0.disconnect()
        if self.btn_c_1.isSignalConnected:
            self.btn_c_1.disconnect()
        if self.btn_c_2.isSignalConnected:
            self.btn_c_2.disconnect()
        if self.btn_c_3.isSignalConnected:
            self.btn_c_3.disconnect()
        if self.btn_c_4.isSignalConnected:
            self.btn_c_4.disconnect()
        if self.btn_c_5.isSignalConnected:
            self.btn_c_5.disconnect()
        if self.btn_c_6.isSignalConnected:
            self.btn_c_6.disconnect()
        if self.btn_c_7.isSignalConnected:
            self.btn_c_7.disconnect()
        if self.btn_c_8.isSignalConnected:
            self.btn_c_8.disconnect()
        if self.btn_c_9.isSignalConnected:
            self.btn_c_9.disconnect()
        if self.btn_c_point.isSignalConnected:
            self.btn_c_point.disconnect()
        if self.btn_c_clear.isSignalConnected:
            self.btn_c_clear.disconnect()
        if self.btn_c_minus.isSignalConnected:
            self.btn_c_minus.disconnect()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

