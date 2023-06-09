from sys import argv, exit
from time import strftime
from os import environ
from functools import partial

import numpy as np
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

        # UI 컴포넌트 불러오기, [계기판 위젯 11개, 초기 화면 로고, 버튼]
        self.ui_list: list = self.ui.getUiList()
        self.connectClickUi(self.ui_list)

        self.status: bool = True
        self.showEnableCalendar()

        # 계기판 인덱스 ( 계기판 클릭 시 각 가지는 인덱스를 의미 )
        self.idx: any = None

        # 데이터 저장 목적
        # date: 오늘 날짜
        # data: 오늘 날짜의 기록된 장치 데이터
        self.model: Model = Model(_date=strftime('%Y.%m.%d'),
                                  _data=getDataNumpy(strftime('%Y%m%d')))

        # 프로그램 시작 시
        # 로고와 계기판 애니메이션 설정
        # effect: 투명 -> 반투명 효과
        # animation: effect를 사용하여 오브젝트가 시간이 지나 서서히 보여짐
        self.effects: list = list(map(self.createOpacityEffect,
                                      [QGraphicsOpacityEffect() for _ in range(12)],
                                      self.ui_list))

        self.animations: list = list(map(self.createAnimation,
                                         [QPropertyAnimation() for _ in range(12)],
                                         self.effects))

        # 초기 스플래시 화면 시작
        # typeOfList: False -> 하나의 오브젝트만 실행
        self.showAnimation(self.animations, typeOfList=False)

        # 초기 화면에 -> 메인 화면으로 이동하여 애니메이션 시작
        # typeOfList: True -> 계기판 위젯들 실행
        self.timer.singleShot(4000, lambda: self.showAnimation(self.animations, typeOfList=True))
        # 6초 뒤 effect, animation 변수 메모리 해제(제거)
        self.timer.singleShot(6000, lambda: self.freeAnimation(self.animations))

        # 쓰레드 불러오기 ( 실제 구현된 것은 아님 )
        self.thread_list = Threads().getThreadList()
        # 계기판과 쓰레드가 각각 연결 되어 실행
        self.timer.singleShot(7500, lambda: self.run(self.ui_list[1:12], self.thread_list))

    # ShowAnimation: 애니메이션 시작
    def showAnimation(self, animation: list, typeOfList: bool = True) -> None:
        if not typeOfList:
            animation[0].start()
            return
        self.ui.page_1.deleteLater()
        for anim in animation[1:]:
            anim.start()

    # noinspection PyMethodMayBeStatic
    # Effect 오브젝트 초기화
    def createOpacityEffect(self, effect: QGraphicsOpacityEffect, ui: QObject) -> QGraphicsOpacityEffect:
        # todo: tool button do not need the effect.
        if ui.objectName() in ['toolButton', 'toolButton_calendar', 'pushButton_update']:
            return NotImplemented
        effect.setOpacity(0)
        ui.setGraphicsEffect(effect)
        return effect

    # noinspection PyMethodMayBeStatic
    # Animation 오브젝트 초기화
    def createAnimation(self, animation: QPropertyAnimation, effect: QGraphicsOpacityEffect) -> QPropertyAnimation:
        animation.setTargetObject(effect)
        animation.setPropertyName(b'opacity')
        animation.setDuration(1500)
        animation.setStartValue(0.0)  # Start location, size
        animation.setEndValue(1.0)  # End location, size
        animation.setEasingCurve(QEasingCurve.InSine)
        return animation

    # noinspection PyMethodMayBeStatic
    # Animation 오브젝트 메모리 해제 ( 일회성 )
    def freeAnimation(self, animation: list) -> None:
        for anim in animation:
            anim.deleteLater()

    # UI 클릭 이벤트
    # Utils/InterfaceClickable 참조
    # 추후 작업은 mouse가 아닌 touch listener로 변경할 것
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
                clickable(ui).connect(self.showEnableCalendar)
                continue
            if ui.objectName() == 'pushButton_update':
                clickable(ui).connect(self.updateChart)
                continue
            # todo: Connect function to switching main scene to chart scene if for other ui.
            idx = int(ui.objectName().split('_')[1])
            clickable(ui).connect(partial(self.switchMain2ChartScreen, idx))

    # 캘린더 출력
    def showEnableCalendar(self) -> None:
        self.status = not self.status
        self.ui.calendarWidget.setVisible(self.status)
        self.ui.pushButton_update.setVisible(self.status)

    # 캘린더에서 임의의 날짜를 선택 후 '차트 갱신' 버튼 클릭 시 차트 리셋 후 재출력
    def updateChart(self) -> None:
        self.showEnableCalendar()
        date: str = self.ui.calendarWidget.selectedDate().toString('yyyy.MM.dd')
        data: np.ndarray = getDataNumpy(date.replace('.', ''))
        self.ui.label_date.setText(date)
        self.ui.widget_chart.removeChart()
        self.timer.singleShot(50, lambda: self.ui.widget_chart.displayChart(data[self.idx-1, :50] if data is not None else None, self.idx))

    # 메인 -> 그래프 화면 이동
    # 각 계기판의 번호에 맞는 데이터가 출력 됨
    def switchMain2ChartScreen(self, idx: int) -> None:
        self.idx: int = idx
        data: np.ndarray = self.model.data
        self.ui.widget_chart.displayChart(data[self.idx-1, : 50] if self.model.data is not None else None, self.idx)
        self.ui.stackedWidget.setCurrentIndex(1)

    # 그래프 -> 메인 화면 이동
    # 메인 화면 이동 시 차트 관련 오브젝트 메모리 해제
    def switchChart2MainScreen(self) -> None:
        self.ui.label_date.setText(self.model.date)
        self.ui.widget_chart.removeChart()
        self.ui.stackedWidget.setCurrentIndex(0)

    # ui와 쓰레드 연결 후 updateInterface 실행
    # widget_4는 역 방향
    def run(self, ui_list: list, thread_list: list) -> None:
        for thr, ui in zip(thread_list, ui_list):
            thr.progress.connect(partial(self.updateInterface, ui, False if ui.objectName() != 'widget_4' else True))

        for thr in thread_list:
            thr.start()

    # todo: Receive from interface thread signal
    @Slot(int)
    def updateInterface(self, obj: QObject, inv: bool, value: int) -> None:
        obj.updateValue(value, inv)

    # esc 키 입력 시 종료
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()

# 화면 고정, 모니터 간 이동 시에 화면 크기가 변동 되어 폰트 크기 등 짤리는 문제 발생
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
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.setFixedSize(1024, 768)
    window.show()

    app.setQuitOnLastWindowClosed(True)
    exit(app.exec_())
