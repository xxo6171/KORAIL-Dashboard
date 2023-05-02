import sys
import time
import numpy as np
from os import environ

from functools import partial
from PySide2.QtCore import Slot, QUrl, QTimer
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtMultimedia import QSoundEffect

from UI.interface_ui import Ui_MainWindow
from Utils.LoadJson import loadJsonStyle
from Utils.InterfaceClickable import clickable
from Utils.DataLogging import getDataNumpyParallel
from InterfaceThread import *
from Model import Model

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        model = Model(_date=time.strftime('%Y%m%d'),
                      _objectId=np.uint8(3),
                      _data=np.array([], dtype=np.uint8))
        print(model)


# Fixed font size by monitor resolution
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == '__main__':
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1040, 728)
    window.show()
    sys.exit(app.exec_())