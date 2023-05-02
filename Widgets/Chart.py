# todo: Visualize graphs of data logged with measurements from CAN devices
# todo: Reading .txt File
from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtCore import QTimer, Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter

class Chart(QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)

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
        chart = QtCharts.QChart()
        series = QtCharts.QLineSeries()

        chart.setTitle(f'Time Series Chart widget_{idx}')
        chart.setTheme(QtCharts.QChart.ChartThemeDark)

        if data is not None:
            for val in data:
                series.append(val[0], val[1])

        # todo: Add the series to the chart
        chart.addSeries(series)

        # Create a QValueAxis for the x-axis
        axis_x = QtCharts.QValueAxis()
        axis_x.setRange(1, 51)
        axis_x.setTickCount(11)
        axis_x.setLabelFormat("%d")

        # Create a QValueAxis for the y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 200)
        axis_y.setTickCount(1)
        axis_y.setLabelFormat("%d")

        # Add the axes to the chart
        chart.addAxis(axis_x, Qt.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignLeft)

        # Attach the series to the axes
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        # Create a QChartView to display the chart
        self.chart_view = QtCharts.QChartView(chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.layout.addWidget(self.chart_view)
        self.setLayout(self.layout)

        if not self.use_timer_event:
            self.update()

    # todo: Update Visualizing by CAN device value
    def updateChart(self):
        self.layout.removeWidget(self.chart_view)