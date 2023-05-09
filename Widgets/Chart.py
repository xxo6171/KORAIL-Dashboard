# todo: Visualize graphs of data logged with measurements from CAN devices
# todo: Reading .txt File
from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtCore import QTimer, Qt, QEasingCurve
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QBrush, QFont, QPen

class Chart(QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.use_timer_event = False
        self.timer = QTimer(self)

        self.chart_view = None
        self.chart = None
        self.series = None
        self.layout = None

        self.font = QFont('NanumSquare')

        self.deviceType = [('차량 속도', 'KM'),
                           ('기관 회전 값', 'RPM'), ('기관 온도', 'ºC'),
                           ('기관 유압', 'BAR'),
                           ('변속기 압력', 'BAR'), ('변속기 온도', 'ºC'),
                           ('제동칸 압력', 'BAR'), ('제동통 압력', 'BAR'),
                           ('주공기 압력', 'BAR'),
                           ('전압', 'V'), ('전류', 'A')]

        if self.use_timer_event:
            self.timer.timeout.connect(self.update)
            self.timer.start(10)
        else:
            self.update()

    def displayChart(self, data, idx):
        self.layout = QVBoxLayout()

        self.chart = QtCharts.QChart()
        self.chart.setTheme(QtCharts.QChart.ChartThemeDark)
        self.chart.setBackgroundBrush(QBrush(Qt.black))
        self.chart.legend().setVisible(False)
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        # InQuint와 반대로 시작 시간이 길고 끝나는 시간이 짧은 뾰족한 애니메이션 (5차 함수)
        self.chart.setAnimationEasingCurve(QEasingCurve.OutQuint)

        title = self.deviceType[idx-1][0]
        unit = self.deviceType[idx-1][1]

        self.chart.setTitle(title)
        title_font = self.chart.titleFont()
        title_font.setFamily(self.font.family())
        title_font.setPointSize(30)
        self.chart.setTitleFont(title_font)

        self.series = QtCharts.QLineSeries()
        self.series.setPen(QPen(Qt.green, 2))
        if data is not None:
            for val in data:
                self.series.append(val[0], val[1])
        self.chart.addSeries(self.series)

        # Create a QValueAxis for the x-axis
        axis_x = QtCharts.QValueAxis()
        axis_x.setRange(1, 51)
        axis_x.setTickCount(11)
        axis_x.setLabelFormat("%d")

        # Create a QValueAxis for the y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 200)
        axis_y.setTickCount(6)
        axis_y.setLabelFormat("%d")

        # Add the axes to the chart
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        self.chart.axisX().setGridLineVisible(False)
        self.chart.axisY().setLineVisible(False)

        for i, axis in enumerate([self.chart.axisX(), self.chart.axisY()]):
            axis_font = axis.labelsFont()
            axis_font.setFamily(self.font.family())
            axis_font.setPointSize(20)
            axis.setLabelsFont(axis_font)
            axis.setTitleFont(axis_font)
            axis.setTitleText("시간" if i == 0 else unit)

        # Attach the series to the axes
        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        # Create a QChartView to display the chart
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

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
