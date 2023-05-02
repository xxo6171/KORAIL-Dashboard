from sys import getsizeof, argv, exit
from time import strftime
import numpy as np
from os import environ

from functools import partial
from PySide2.QtCore import Slot, QUrl, QTimer
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtMultimedia import QSoundEffect

from UI.interface_ui import Ui_MainWindow
from Utils.LoadJson import loadJsonStyle
from Utils.InterfaceClickable import clickable
from Utils.DataLogging import getDataNumpy
from InterfaceThread import *
from Model import Model

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

        self.model = Model(_date=strftime('%Y%m%d'),
                           _data=getDataNumpy(strftime('%Y%m%d')))

        self.ui_list: list = self.ui.getUiList()
        self.connectClickUi(self.ui_list, self.ui.pushButton)

    # UI 클릭 이벤트 처리
    def connectClickUi(self, ui_list, button) -> None:
        for ui in ui_list:
            idx = np.uint8(ui.objectName().split('_')[1])
            clickable(ui).connect(partial(self.switchMain2GraphScreen, idx))
        clickable(button).connect(self.switchGraph2MainScreen)

    # 계기판 위젯 클릭 시 그래프 화면 이동
    def switchMain2GraphScreen(self, idx) -> None:
        self.model.objectId = idx
        data = self.model.data[self.model.objectId-1, : 50]
        chart = self.ui.widget_chart
        stack = self.ui.stackedWidget

        chart.displayChart(data, self.model.objectId)
        stack.setCurrentIndex(1)

    # 뒤로 가기 버튼 클릭 시 메인 화면 이동
    def switchGraph2MainScreen(self) -> None:
        stack = self.ui.stackedWidget
        chart = self.ui.widget_chart

        stack.setCurrentIndex(0)
        chart.updateChart()

# 폰트 크기 고정 ( 화면 크기가 다를 시 발생 하는 문제 해결 )
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == '__main__':
    suppress_qt_warnings()
    app = QApplication(argv)
    window = MainWindow()
    window.setFixedSize(1040, 728)
    window.show()
    exit(app.exec_())