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

        self.ui_list = self.ui.getUiList()
        self.connectClickUi(self.ui_list, self.ui.pushButton)

        # Create ui(interface)'s threads
        self.t1, self.t2, self.t3, self.t4, self.t5, \
            self.t6, self.t7, self.t8, self.t9, self.t10, self.t11 = Thread1(self), Thread2(self), Thread3(self), Thread4(self), Thread5(self), \
            Thread6(self), Thread7(self), Thread8(self), Thread9(self), Thread10(self), Thread11(self)

        self.thread_list = [self.t1, self.t2, self.t3, self.t4, self.t5,
                            self.t6, self.t7, self.t8, self.t9, self.t10, self.t11]

        self.run(self.ui_list, self.thread_list)

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

    # todo: Executing Interface thread
    def run(self, ui_list: list, thread_list: list):
        for _thr, _ui in zip(thread_list, ui_list):
            _thr.progress.connect(partial(self.updateInterface, _ui, None if _ui.objectName() != 'widget_4' else 'inverse'))

        for _thr in thread_list:
            _thr.start()

    # todo: Receive from interface thread signal
    @Slot(int)
    def updateInterface(self, obj: object, flag: str, value: int):
        obj.updateValue(value, flag=flag)

# 폰트 크기 고정 ( 화면 크기가 다를 시 발생 하는 문제 해결 )
def suppress_qt_warnings() -> None:
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