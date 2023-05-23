# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacefeRpOl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Widgets.AnalogGaugeWidget import AnalogGaugeWidget
from Widgets.AnalogLinearGaugeWidget import AnalogLinearGaugeWidget
from Widgets.Chart import Chart

import Images.korail

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 768)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:reflect, x1:0.506, y1:0.523, x2:1, y2:1, stop:0.281755 rgba(15, 15, 15, 255), stop:1 rgba(22, 52, 83, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1024, 768))
        self.stackedWidget.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 260, 881, 231))
        self.label.setStyleSheet(u"image: url(:/newPrefix/korail.png);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.widget_1 = AnalogGaugeWidget(self.page_3)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setEnabled(True)
        self.widget_1.setGeometry(QRect(40, 10, 280, 240))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.widget_1.setMaximumSize(QSize(1042, 16777215))
        self.widget_1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_2 = AnalogGaugeWidget(self.page_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QRect(360, 10, 310, 270))
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(1042, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_7 = AnalogGaugeWidget(self.page_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setEnabled(True)
        self.widget_7.setGeometry(QRect(360, 590, 310, 160))
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMaximumSize(QSize(1042, 16777215))
        self.widget_7.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_5 = AnalogGaugeWidget(self.page_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setEnabled(True)
        self.widget_5.setGeometry(QRect(360, 290, 310, 290))
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QSize(1042, 16777215))
        self.widget_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_6 = AnalogGaugeWidget(self.page_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        self.widget_6.setGeometry(QRect(690, 260, 250, 250))
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMaximumSize(QSize(1042, 16777215))
        self.widget_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_11 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(700, 610, 320, 60))
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_8 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 520, 320, 60))
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_9 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(10, 610, 320, 60))
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_10 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(700, 520, 320, 60))
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_3 = AnalogGaugeWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QRect(710, 10, 280, 240))
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(1042, 16777215))
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget_4 = AnalogGaugeWidget(self.page_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QRect(90, 260, 250, 250))
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(1042, 16777215))
        self.widget_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_chart = Chart(self.page_4)
        self.widget_chart.setObjectName(u"widget_chart")
        self.widget_chart.setGeometry(QRect(0, 0, 1024, 768))
        self.widget_chart.setStyleSheet(u"")
        self.label_date = QLabel(self.page_4)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(730, 30, 221, 31))
        self.label_date.setStyleSheet(u"color: white;\n"
"font: 24pt HDharmony B;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_date.setAlignment(Qt.AlignCenter)
        self.toolButton = QToolButton(self.page_4)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(10, 20, 80, 41))
        self.toolButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px")
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(Qt.LeftArrow)
        self.toolButton_calendar = QToolButton(self.page_4)
        self.toolButton_calendar.setObjectName(u"toolButton_calendar")
        self.toolButton_calendar.setGeometry(QRect(950, 30, 50, 31))
        self.toolButton_calendar.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px")
        self.toolButton_calendar.setAutoRaise(False)
        self.toolButton_calendar.setArrowType(Qt.NoArrow)
        self.calendarWidget = QCalendarWidget(self.page_4)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(539, 70, 461, 351))
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QToolButton{\n"
"	height: 40px;\n"
"	color: black;\n"
"}\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth{\n"
"	width: 50px;\n"
"	background-color: gray;\n"
"}\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth{\n"
"	width: 50px;\n"
"	background-color: gray;\n"
"}\n"
"QCalendarWidget QToolButton::hover{\n"
"	background-color: gray;\n"
"}\n"
"QCalendarWidget QWidget{\n"
"	font: 18pt HDharmony M;\n"
"	alternate-background-color: rgb(220,220,220);\n"
"	background-color: rgba(180, 180, 180);\n"
"}\n"
"")
        self.calendarWidget.setFirstDayOfWeek(Qt.Sunday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.pushButton_update = QPushButton(self.page_4)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setGeometry(QRect(540, 420, 461, 41))
        self.pushButton_update.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	font: 18pt HDharmony M;\n"
"	background-color: rgba(220, 220, 220);\n"
"}")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        from time import strftime
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        # self.label_loading.setText(QCoreApplication.translate("MainWindow", u"LOADING...", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", strftime(u"%Y.%m.%d"), None))
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"\ucc28\ud2b8 \uac31\uc2e0", None))
    # retranslateUi

    def getUiList(self):
        return [self.label, self.widget_1, self.widget_2, self.widget_3, self.widget_4, self.widget_5,
                self.widget_6, self.widget_7, self.widget_8, self.widget_9, self.widget_10, self.widget_11, self.toolButton,
                self.toolButton_calendar, self.pushButton_update]

