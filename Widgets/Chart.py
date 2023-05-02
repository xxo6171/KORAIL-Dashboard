# todo: Visualize graphs of data logged with measurements from CAN devices
# todo: Reading .txt File
from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtCore import QTimer, Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter

class Chart(QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)

        self.axis_x = None
        self.axis_y = None

        self.chart = None
        self.series = None
        self.chart_view = None

        # Set up the layout and add the chart view
        self.layout = QVBoxLayout()
        self.use_timer_event = False
        self.timer = QTimer(self)

        if self.use_timer_event:
            self.timer.timeout.connect(self.update)
            self.timer.start(10)
        else:
            self.update()

    def displayChart(self, data, idx):
        self.chart = QtCharts.QChart()
        self.series = QtCharts.QLineSeries()

        self.chart.setTitle(f'Time Series Chart widget_{idx}')
        self.chart.setTheme(QtCharts.QChart.ChartThemeDark)

        if data is not None:
            for val in data:
                self.series.append(val[0], val[1])

        # todo: Add the series to the chart
        self.chart.addSeries(self.series)

        # Create a QValueAxis for the x-axis
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setRange(1, 51)
        self.axis_x.setTickCount(11)
        self.axis_x.setLabelFormat("%d")

        # Create a QValueAxis for the y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setRange(0, 200)
        self.axis_y.setTickCount(1)
        self.axis_y.setLabelFormat("%d")

        # Add the axes to the chart
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        # Attach the series to the axes
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        # Create a QChartView to display the chart
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.layout.addWidget(self.chart_view)
        self.setLayout(self.layout)

        if not self.use_timer_event:
            self.update()

    # todo: Update Visualizing by CAN device value
    def updateChart(self):
        self.layout.removeWidget(self.chart_view)