import math
import numpy as np

try:
    from PySide2.QtWidgets import QMainWindow, QWidget, QApplication

    from PySide2.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient, \
    QRadialGradient, QFontDatabase, QTransform

    from PySide2.QtCore import Qt, QTime, QTimer, QPoint, QPointF, QRect, QSize, QObject, Signal, QRectF
except:
    print("Error while importing PySide2")
    exit()

class DashBoard(QWidget):
    def __init__(self, parent=None):
        super(DashBoard, self).__init__(parent)
    #     print(self.width())
    #     print(self.height())
    #
    #     # self.outer_radius = np.int16((self.height() / 2) - 50)
    #     # self.inner_radius = np.int16((self.height() / 2) - 20)
    #
    #     self.outer_radius = (self.height() / 2) - 50
    #     self.inner_radius = (self.height() / 2) - 20
    #
    #     self.setStyleSheet("background-color: black;")
    #
    # # def initUI(self):
    # #     self.setGeometry(500, 500, 630, 200)
    # #     self.setWindowTitle('Drawing Rectangles')
    # #     self.show()
    #
    # def paintEvent(self, event):
    #     qp = QPainter()
    #     qp.setRenderHint(QPainter.Antialiasing)
    #     qp.begin(self)
    #     qp.translate(self.width() / 2, self.height() / 2)
    #     self.drawOuterCircle(qp)
    #     # self.drawInnerCircle(qp)
    #     qp.end()
    #
    # def drawOuterCircle(self, qp):
    #     qp.setPen(QPen(Qt.white))
    #     # Circle
    #     points = QPolygonF()
    #     for i in range(120, 421):
    #         x = np.int16(self.outer_radius * math.cos(math.radians(i)))
    #         y = np.int16(self.outer_radius * math.sin(math.radians(i)))
    #         print(QPointF(x, y))
    #         points.append(QPointF(x, y))
    #     qp.drawPolygon(points)  # 원 그리기
    #
    # def drawInnerCircle(self, qp):
    #     qp.setPen(QPen(Qt.white))
    #     points = QPolygonF()
    #     for i in range(0, 360, 5):
    #         x = self.inner_radius * math.cos(math.radians(i))
    #         y = self.inner_radius * math.sin(math.radians(i))
    #         points.append(QPointF(x, y))
    #     qp.drawPolygon(points)  # 원 그리기

if __name__ == '__main__':
    app = QApplication([])
    window = DashBoard()
    window.show()
    app.exec_()
