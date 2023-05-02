from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QBrush, QPen, QLinearGradient, QPolygon, QFont, QFontDatabase
from PySide2.QtCore import Qt, QPoint, QTimer, Signal


class AnalogLinearGaugeWidget(QWidget):
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super(AnalogLinearGaugeWidget, self).__init__(parent)
        # self.initUI()
        # Initialize value
        self.animation = None
        self.x, self.y = 10, 30
        self.width, self.height = 300, 10

        self.units = "Units"
        self.minValue = 0
        self.maxValue = 100
        self.value = self.minValue

        self.needle_x = 10
        self.needle_y = self.y + self.height
        self.needle_point = [QPoint(self.needle_x, self.needle_y),
                             QPoint(self.needle_x - 10, self.needle_y + 10),
                             QPoint(self.needle_x + 10, self.needle_y + 10)]
        # Set the Font Family
        self.fontDB = QFontDatabase()
        self.font_id = self.fontDB.addApplicationFont('Fonts/DS-DIGIB.TTF')
        self.font_family = self.fontDB.applicationFontFamilies(self.font_id)[0]

        # Set the UI repaint event
        self.use_timer_event = False
        self.timer = QTimer(self)

        if self.use_timer_event:
            self.timer.timeout.connect(self.update)
            self.timer.start(10)
        else:
            self.update()

    #
    # def initUI(self):
    #     self.setGeometry(500, 500, 630, 200)
    #     self.setWindowTitle('Drawing Rectangles')
    #     self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        self.drawUnitsText(qp)
        self.drawValueText(qp)
        self.drawScale(qp)
        self.drawNeedle(qp)
        qp.end()

    # Drawing the Rectangle Bar
    def drawRectangles(self, qp):
        qp.setPen(QPen(Qt.NoPen))
        grad = QLinearGradient(self.x, self.y, self.width, self.height)
        grad.setColorAt(0.0, Qt.green)
        grad.setColorAt(0.5, Qt.yellow)
        grad.setColorAt(1.0, Qt.red)
        qp.setBrush(QBrush(grad))
        qp.drawRect(self.x, self.y, self.width, self.height)

    # Drawing the units text
    def drawUnitsText(self, qp):
        qp.setPen(QPen(Qt.white, 1, Qt.SolidLine))
        qp.setFont(QFont("Courier New", 13))
        qp.drawText(self.x, self.height+10, self.units)

    # Drawing the value text
    def drawValueText(self, qp):
        qp.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        qp.setFont(QFont(self.font_family, 15))
        qp.drawText(self.x + 100, self.height+10, str(self.value))

    # Drawing the scale value
    def drawScale(self, qp):
        qp.setPen(QPen(Qt.gray, 1, Qt.SolidLine))
        for i in range(self.minValue, self.maxValue+1):
            scale_x = i * (self.width // self.maxValue) + self.x
            # if i == 0 or i == self.maxValue:
            #     # qp.setPen(QPen(Qt.white, 1, Qt.SolidLine))
            #     qp.setFont(QFont(self.font_family, 10))
            #     qp.drawText(scale_x, self.height + 70, str(i))
            #     continue
            if i == 0 or i == self.maxValue:
                qp.setFont(QFont(self.font_family, 9))
                qp.drawText(scale_x, self.height + 50, str(i))
                continue
            if i % 10 == 0:
                qp.drawLine(scale_x, self.y, scale_x, self.y + 10)
                qp.setFont(QFont(self.font_family, 9))
                qp.drawText(scale_x, self.height + 50, str(i))
                continue
            qp.drawLine(scale_x, self.y, scale_x, self.y + 5)

    # Drawing a needle pointer in the shape of a triangle
    def drawNeedle(self, qp):
        qp.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.red))
        qp.drawPolygon(QPolygon(self.needle_point))

    # Update Value
    def updateValue(self, value, flag=None):
        if value >= self.maxValue:
            self.value = self.maxValue
        elif value <= self.minValue:
            self.value = self.minValue
        else:
            self.value = value

        x = self.value * (self.width // self.maxValue) + self.needle_x
        self.needle_point = [QPoint(x, self.needle_y),
                             QPoint(x-10, self.needle_y+10),
                             QPoint(x+10, self.needle_y+10)]

        self.valueChanged.emit(int(value))

        if not self.use_timer_event:
            self.timer.start(1500)
            self.update()

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Right:
    #         self.updateValue(self.value + 1)
    #     if e.key() == Qt.Key_Left:
    #         self.updateValue(self.value - 1)

# if __name__ == '__main__':
#     app = QApplication([])
#     window = AnalogLinearGaugeWidget()
#     window.show()
#     app.exec_()