import os.path
from sys import argv, exit
from time import strftime
from os import environ
from os.path import isfile

from functools import partial

import numpy
from PySide2.QtCore import Slot, QUrl, QTimer, QPropertyAnimation, QEasingCurve, QObject
from PySide2.QtGui import Qt, QKeyEvent
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
        self.timer: QTimer = QTimer()

        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

        self.ui_list: list = self.ui.getUiList()
        self.connectClickUi(self.ui_list)

        self.status: bool = True
        self.enableCalendar()

        self.idx: any = None

        self.model: Model = Model(_date=strftime('%Y.%m.%d'),
                                  _data=getDataNumpy(strftime('%Y%m%d')))

        self.effects: list = list(map(self.createOpacityEffect,
                                      [QGraphicsOpacityEffect() for _ in range(12)],
                                      self.ui_list))

        self.animations: list = list(map(self.createAnimation,
                                         [QPropertyAnimation() for _ in range(12)],
                                         self.effects))

        self.showAnimation(self.animations, typeOfList=False)
        self.timer.singleShot(4000, lambda: self.showAnimation(self.animations, typeOfList=True))
        self.timer.singleShot(6000, lambda: self.freeAnimation(self.animations))

        #
        # self.thread_list = Threads().getThreadList()
        # self.timer.singleShot(7500, lambda: self.run(self.ui_list, self.thread_list))

    # todo: Show animation on splash and main screen
    def showAnimation(self, animation: list, typeOfList: bool = True) -> None:
        if not typeOfList:
            animation[0].start()
            return
        self.ui.page_1.deleteLater()
        for anim in animation[1:]:
            anim.start()

    # noinspection PyMethodMayBeStatic
    # todo: Create opacity effect by widgets and set the ui from opacity effect.
    def createOpacityEffect(self, effect: QGraphicsOpacityEffect, ui: QObject) -> QGraphicsOpacityEffect:
        # todo: tool button do not need the effect.
        if ui.objectName() in ['toolButton', 'toolButton_calendar', 'pushButton_update']:
            return NotImplemented
        effect.setOpacity(0)
        ui.setGraphicsEffect(effect)
        return effect

    # noinspection PyMethodMayBeStatic
    # todo: Create animation by widgets and set the animation options.
    def createAnimation(self, animation: QPropertyAnimation, effect: QGraphicsOpacityEffect) -> QPropertyAnimation:
        animation.setTargetObject(effect)
        animation.setPropertyName(b'opacity')
        animation.setDuration(1500)
        animation.setStartValue(0.0)  # Start location, size
        animation.setEndValue(1.0)  # End location, size
        animation.setEasingCurve(QEasingCurve.InSine)
        return animation

    # noinspection PyMethodMayBeStatic
    # todo: Animation and Effect variables are One-off. Effect variables are automatically free after finishing operate.
    def freeAnimation(self, animation: list) -> None:
        for anim in animation:
            anim.deleteLater()

    # todo: Ui click event.
    def connectClickUi(self, ui_list: list) -> None:
        for ui in ui_list:
            # todo: Nothing works if ui is label logo.
            if ui.objectName() == 'label':
                continue
            # todo: Connect function to switching graph scene to main scene if ui is toolButton.
            if ui.objectName() == 'toolButton':
                clickable(ui).connect(self.switchChart2MainScreen)
                continue
            if ui.objectName() == 'toolButton_calendar':
                clickable(ui).connect(self.enableCalendar)
                continue
            if ui.objectName() == 'pushButton_update':
                clickable(ui).connect(self.updateChart)
                continue
            # todo: Connect function to switching main scene to chart scene if for other ui.
            idx = int(ui.objectName().split('_')[1])
            clickable(ui).connect(partial(self.switchMain2ChartScreen, idx))

    def enableCalendar(self) -> None:
        self.status = not self.status
        self.ui.calendarWidget.setVisible(self.status)
        self.ui.pushButton_update.setVisible(self.status)

    def updateChart(self) -> None:
        self.enableCalendar()
        date: str = self.ui.calendarWidget.selectedDate().toString('yyyy.MM.dd')
        data: numpy.ndarray = getDataNumpy(date.replace('.', ''))[self.idx-1, :50]
        self.ui.label_date.setText(date)
        self.ui.widget_chart.removeChart()
        self.timer.singleShot(100, lambda: self.ui.widget_chart.displayChart(data if data is not None else None, self.idx))

    # todo: Switching main to chart scene when click the widget.
    def switchMain2ChartScreen(self, idx: int) -> None:
        self.idx = idx
        self.ui.widget_chart.displayChart(self.model.data[self.idx-1, : 50] if self.model.data is not None else None, self.idx)
        self.ui.stackedWidget.setCurrentIndex(1)

    # todo: Switching chart to main scene when click the tool button.
    def switchChart2MainScreen(self) -> None:
        self.ui.label_date.setText(self.model.date)
        self.ui.widget_chart.removeChart()
        self.ui.stackedWidget.setCurrentIndex(0)

    # todo: Executing Interface thread
    def run(self, ui_list: list, thread_list: list) -> None:
        for thr, ui in zip(thread_list, ui_list):
            thr.progress.connect(partial(self.updateInterface, ui, False if ui.objectName() != 'widget_4' else True))

        for thr in thread_list:
            thr.start()

    # todo: Receive from interface thread signal
    @Slot(int)
    def updateInterface(self, obj: QObject, inv: bool, value: int) -> None:
        obj.updateValue(value, inv)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()

# todo: Fix font size: For issues that occur when screen sizes are not the same.
def suppress_qt_warnings() -> None:
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == '__main__':
    suppress_qt_warnings()
    app: QApplication = QApplication(argv)
    window: MainWindow = MainWindow()
    # window.setFixedSize(1680, 1050)
    # window.showFullScreen()
    # window.setWindowFlags(Qt.FramelessWindowHint)
    window.setFixedSize(1024, 768)
    window.show()

    app.setQuitOnLastWindowClosed(True)
    exit(app.exec_())
