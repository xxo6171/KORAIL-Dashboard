# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceMzjYBo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from time import strftime
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
        MainWindow.resize(1040, 728)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1040, 728))
        self.stackedWidget.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 190, 881, 231))
        self.label.setStyleSheet(u"image: url(:/newPrefix/korail.png);")
        self.label.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.page_1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(160, 480, 731, 15))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Consolas\";\n"
"	border-radius: 30px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 228, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.page_1)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setEnabled(True)
        self.label_loading.setGeometry(QRect(280, 510, 501, 41))
        self.label_loading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Consolas\";")
        self.label_loading.setAlignment(Qt.AlignCenter)
        # self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget_1 = AnalogGaugeWidget(self.page_3)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setEnabled(True)
        self.widget_1.setGeometry(QRect(40, 20, 250, 250))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.widget_1.setMaximumSize(QSize(1042, 16777215))
        self.widget_2 = AnalogGaugeWidget(self.page_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QRect(360, 20, 330, 260))
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(1042, 16777215))
        self.widget_7 = AnalogGaugeWidget(self.page_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setEnabled(True)
        self.widget_7.setGeometry(QRect(370, 570, 310, 150))
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMaximumSize(QSize(1042, 16777215))
        self.widget_5 = AnalogGaugeWidget(self.page_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setEnabled(True)
        self.widget_5.setGeometry(QRect(390, 290, 270, 260))
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QSize(1042, 16777215))
        self.widget_6 = AnalogGaugeWidget(self.page_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        self.widget_6.setGeometry(QRect(700, 280, 210, 200))
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMaximumSize(QSize(1042, 16777215))
        self.widget_11 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(700, 570, 330, 70))
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_8 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(20, 490, 330, 70))
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_9 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(20, 570, 330, 70))
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_10 = AnalogLinearGaugeWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(700, 490, 330, 70))
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_3 = AnalogGaugeWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QRect(760, 20, 250, 250))
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(1042, 16777215))
        self.widget_4 = AnalogGaugeWidget(self.page_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QRect(140, 280, 210, 200))
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(1042, 16777215))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_chart = Chart(self.page_4)
        self.widget_chart.setObjectName(u"widget_chart")
        self.widget_chart.setGeometry(QRect(0, 70, 1040, 651))
        self.pushButton = QPushButton(self.page_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 80, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"font: 14pt \"Arial\";\n"
"background-color: rgb(255, 0, 0);")
        self.label_date = QLabel(self.page_4)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(810, 30, 221, 31))
        self.label_date.setStyleSheet(u"color: white;\n"
"font: 24pt Malgon Gothic;")
        self.label_date.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        from time import strftime
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_loading.setText(QCoreApplication.translate("MainWindow", u"LOADING...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", strftime(u"%Y.%m.%d"), None))
    # retranslateUi

    def getUiList(self):
        return [self.widget_1, self.widget_2, self.widget_3, self.widget_4, self.widget_5,
                self.widget_6, self.widget_7, self.widget_8, self.widget_9, self.widget_10, self.widget_11]