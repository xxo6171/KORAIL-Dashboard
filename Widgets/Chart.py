# todo: Visualize graphs of data logged with measurements from CAN devices
# todo: Reading .txt File
import random

from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtCore import QTimer, Qt, QEasingCurve
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QBrush, QFont, QPen


class Chart(QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.use_timer_event: bool = False
        self.timer: QTimer = QTimer(self)

        self.chart_view: object = None
        self.chart: object = None
        self.series: object = None
        self.series2: object = None
        self.layout: object = None

        self.font: QFont = QFont('HDharmony M')

        self.deviceType: list = [('차량 속도', '속도 (km/h)'),
                                 ('기관 회전 값', 'rpm '), ('기관 온도', '온도 (ºC)'),
                                 ('기관 유압', '압력 (bar)'),
                                 ('변속기 압력', '압력 (bar)'), ('변속기 온도', '온도 (ºC)'),
                                 ('제동칸 압력', '압력 (bar)'), ('제동통 압력', '압력 (bar)'),
                                 ('주공기 압력', '압력 (bar)'),
                                 ('전압', 'V '), ('전류', 'A ')]

        if self.use_timer_event:
            self.timer.timeout.connect(self.update)
            self.timer.start(10)
        else:
            self.update()

    def displayChart(self, data: list, idx: int):
        self.chart: QtCharts.QChart = QtCharts.QChart()
        self.chart.setTheme(QtCharts.QChart.ChartThemeDark)
        self.chart.setBackgroundBrush(QBrush(Qt.transparent))
        self.chart.legend().setVisible(False)
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chart.setAnimationEasingCurve(QEasingCurve.OutQuint)

        title: str = self.deviceType[idx-1][0]
        unit: str = self.deviceType[idx-1][1]
        unit2: str = '온도'

        self.chart.setTitle(title)
        title_font: QtCharts.QChart.titleFont = self.chart.titleFont()
        title_font.setFamily(self.font.family())
        title_font.setPointSize(30)
        self.chart.setTitleFont(title_font)

        self.series: QtCharts.QLineSeries = QtCharts.QLineSeries()
        self.series.setName(unit.split()[0])
        self.series.setPen(QPen(Qt.cyan, 2))
        if data is not None:
            for val in data:
                self.series.append(val[0], val[1])
        self.chart.addSeries(self.series)

        if '압' in unit:
            self.series2 = QtCharts.QLineSeries()
            self.series2.setName(unit2)

            self.series2.setPen(QPen(Qt.red, 2))
            for i in range(1, 51):
                value = random.randrange(20, 50)
                self.series2.append(i, value)
            self.chart.addSeries(self.series2)

        # Create a QValueAxis for the x-axis
        axis_x: QtCharts.QValueAxis = QtCharts.QValueAxis()
        axis_x.setRange(1, 51)
        axis_x.setTickCount(11)
        axis_x.setLabelFormat("%d")

        # Create a QValueAxis for the y-axis
        axis_y: QtCharts.QValueAxis = QtCharts.QValueAxis()
        axis_y.setRange(0, 200)
        axis_y.setTickCount(6)
        axis_y.setLabelFormat("%d")

        axis_y2: QtCharts.QValueAxis = QtCharts.QValueAxis()
        axis_y2.setRange(0, 100)
        axis_y2.setTickCount(6)
        axis_y2.setLabelFormat("%d")

        # Add the axes to the chart
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignLeft)

        axis_x.setGridLineVisible(False)
        axis_y.setLineVisible(False)

        if '압' in unit:
            self.chart.addAxis(axis_y2, Qt.AlignRight)
            axis_y2.setLineVisible(False)

        axis_list = [axis_x, axis_y]
        if '압' in unit:
            axis_list.append(axis_y2)

        for i, axis in enumerate(axis_list):
            axis_font = axis.labelsFont()
            axis_font.setFamily(self.font.family())
            axis_font.setPointSize(20)
            axis.setLabelsFont(axis_font)
            axis.setTitleFont(axis_font)
            if i == 0:
                axis.setTitleText("시간")
                continue
            if i == 1:
                axis.setTitleText(unit)
            if i == 2:
                axis.setTitleText(unit2)
            # axis.setTitleText("시간" if i == 0 else unit)

        # Attach the series to the axes
        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        if '압' in unit:
            self.series2.attachAxis(axis_x)
            self.series2.attachAxis(axis_y2)
            legend: QtCharts.QChart.legend = self.chart.legend()
            legend.setFont(QFont(self.font.family(), 15))
            legend.setAlignment(Qt.AlignTop)
            legend.setVisible(True)

        # Create a QChartView to display the chart
        self.chart_view: QtCharts.QChartView = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.HighQualityAntialiasing)

        self.layout: QVBoxLayout = QVBoxLayout()
        self.layout.addWidget(self.chart_view)
        self.setLayout(self.layout)

        if not self.use_timer_event:
            self.update()

    # 메모리 해제
    def removeChart(self):
        # 메모리 해제
        self.chart.deleteLater()
        self.chart_view.deleteLater()
        self.layout.deleteLater()

