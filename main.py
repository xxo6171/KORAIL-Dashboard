from sys import getsizeof, argv, exit
from time import strftime
from os import environ

import numpy as np

from functools import partial
from PySide2.QtCore import Slot, QUrl, QTimer, QPropertyAnimation, QEasingCurve
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect
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
        self.timer = QTimer()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

        self.ui_list = self.ui.getUiList()
        self.connectClickUi(self.ui_list, self.ui.toolButton)

        self.effect_list = self.getEffectVarList()
        self.animation_list = self.getAnimationVarList()

        self.animationShowSplash()
        self.timer.singleShot(4000, lambda: self.animationShowWidget(self.ui_list, self.effect_list, self.animation_list))

        self.model = Model(_date=strftime('%Y%m%d'),
                           _data=getDataNumpy(strftime('%Y%m%d')))

        self.thread_list = Threads().getThreadList()
        # self.timer.singleShot(7500, lambda: self.run(self.ui_list, self.thread_list))

    def animationShowSplash(self):
        self.opacity_effect_logo = QGraphicsOpacityEffect()
        self.animation_logo = QPropertyAnimation(self.opacity_effect_logo, b'opacity')

        self.opacity_effect_logo.setOpacity(0)
        self.ui.label.setGraphicsEffect(self.opacity_effect_logo)
        self.animation_logo.setDuration(1500)
        self.animation_logo.setStartValue(0.0)  # 시작 위치와 크기
        self.animation_logo.setEndValue(1.0)  # 종료 위치와 크기
        self.animation_logo.setEasingCurve(QEasingCurve.InSine)
        self.animation_logo.start()
        self.timer.singleShot(4000, lambda: self.ui.page_1.deleteLater())

    # noinspection PyMethodMayBeStatic
    def animationShowWidget(self, ui_list, effect_list, animation_list):
        for ui, effect, anim in zip(ui_list, effect_list, animation_list):
            effect.setOpacity(0)
            ui.setGraphicsEffect(effect)
            anim.setDuration(1800)
            anim.setStartValue(0.0)
            anim.setEndValue(1.0)
            # anim.setEasingCurve(QEasingCurve.InExpo)
            anim.setEasingCurve(QEasingCurve.InSine)
            anim.start()

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

        self.ui.widget_chart.displayChart(data, object_id)
        self.ui.stackedWidget.setCurrentIndex(1)

    # 뒤로 가기 버튼 클릭 시 메인 화면 이동
    def switchGraph2MainScreen(self) -> None:
        self.ui.widget_chart.removeChart()
        self.ui.stackedWidget.setCurrentIndex(0)

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

    def getEffectVarList(self):
        self.opacity_effect_1 = QGraphicsOpacityEffect()
        self.opacity_effect_2 = QGraphicsOpacityEffect()
        self.opacity_effect_3 = QGraphicsOpacityEffect()
        self.opacity_effect_4 = QGraphicsOpacityEffect()
        self.opacity_effect_5 = QGraphicsOpacityEffect()
        self.opacity_effect_6 = QGraphicsOpacityEffect()
        self.opacity_effect_7 = QGraphicsOpacityEffect()
        self.opacity_effect_8 = QGraphicsOpacityEffect()
        self.opacity_effect_9 = QGraphicsOpacityEffect()
        self.opacity_effect_10 = QGraphicsOpacityEffect()
        self.opacity_effect_11 = QGraphicsOpacityEffect()

        return [self.opacity_effect_1, self.opacity_effect_2, self.opacity_effect_3, self.opacity_effect_4,
                self.opacity_effect_5, self.opacity_effect_6, self.opacity_effect_7, self.opacity_effect_8,
                self.opacity_effect_9, self.opacity_effect_10, self.opacity_effect_11]

    def getAnimationVarList(self):
        self.animation_1 = QPropertyAnimation(self.opacity_effect_1, b'opacity')
        self.animation_2 = QPropertyAnimation(self.opacity_effect_2, b'opacity')
        self.animation_3 = QPropertyAnimation(self.opacity_effect_3, b'opacity')
        self.animation_4 = QPropertyAnimation(self.opacity_effect_4, b'opacity')
        self.animation_5 = QPropertyAnimation(self.opacity_effect_5, b'opacity')
        self.animation_6 = QPropertyAnimation(self.opacity_effect_6, b'opacity')
        self.animation_7 = QPropertyAnimation(self.opacity_effect_7, b'opacity')
        self.animation_8 = QPropertyAnimation(self.opacity_effect_8, b'opacity')
        self.animation_9 = QPropertyAnimation(self.opacity_effect_9, b'opacity')
        self.animation_10 = QPropertyAnimation(self.opacity_effect_10, b'opacity')
        self.animation_11 = QPropertyAnimation(self.opacity_effect_11, b'opacity')

        return [self.animation_1, self.animation_2, self.animation_3, self.animation_4,
                self.animation_5, self.animation_6, self.animation_7, self.animation_8,
                self.animation_9, self.animation_10, self.animation_11]

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
    # window.setWindowFlags(Qt.FramelessWindowHint)
    window.setFixedSize(1024, 768)
    window.show()

    app.setQuitOnLastWindowClosed(True)
    exit(app.exec_())