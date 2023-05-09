from sys import getsizeof, argv, exit
from time import strftime
import numpy as np
from os import environ

from functools import partial
from PySide2.QtCore import Slot, QUrl, QTimer
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtMultimedia import QSoundEffect

from UI.interface_ui import Ui_MainWindow
from Utils.LoadJson import loadJsonStyle
from Utils.InterfaceClickable import clickable
from Utils.DataLogging import getDataNumpy
from InterfaceThread import Threads
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

        self.thread_list = Threads().getThreadList()
        self.run(self.ui_list, self.thread_list)

    # UI 클릭 이벤트 처리
    def connectClickUi(self, ui_list, btn_back) -> None:
        for ui in ui_list:
            idx = np.uint8(ui.objectName().split('_')[1])
            clickable(ui).connect(partial(self.switchMain2GraphScreen, idx))
        clickable(btn_back).connect(self.switchGraph2MainScreen)

    # 계기판 위젯 클릭 시 그래프 화면 이동
    def switchMain2GraphScreen(self, idx) -> None:
        data = None
        object_id = idx

        if self.model.data is not None:
            data = self.model.data[object_id-1, : 50]

        chart = self.ui.widget_chart
        chart.displayChart(data, object_id)

        stack = self.ui.stackedWidget
        stack.setCurrentIndex(1)

    # 뒤로 가기 버튼 클릭 시 메인 화면 이동
    def switchGraph2MainScreen(self) -> None:
        chart = self.ui.widget_chart
        chart.removeChart()

        stack = self.ui.stackedWidget
        stack.setCurrentIndex(0)

    # todo: Executing Interface thread
    def run(self, ui_list, thread_list) -> None:
        for thr, ui in zip(thread_list, ui_list):
            thr.progress.connect(partial(self.updateInterface, ui, False if ui.objectName() != 'widget_4' else True))

        for thr in thread_list:
            thr.start()

    # todo: Receive from interface thread signal
    @Slot(int)
    def updateInterface(self, obj: object, inv: bool, value: int) -> None:
        obj.updateValue(value, inv)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

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
    # window.setFixedSize(1680, 1050)
    # window.showFullScreen()
    window.setFixedSize(1040, 728)
    window.show()

    app.setQuitOnLastWindowClosed(True)
    exit(app.exec_())