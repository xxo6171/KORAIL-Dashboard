from PySide2.QtCore import QThread, Signal
# import random
import time

class Thread1(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 81):
        #     self.progress.emit(i)
        #     time.sleep(0.01)
        # for i in range(80, -1, -1):
        #     self.progress.emit(i)
        #     time.sleep(0.01)

        # while True:
        #     for i in range(0, 81):
        #         self.progress.emit(i)
        #         time.sleep(0.02)
        #     for i in range(80, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.02)
        # self.finished.emit()

class Thread2(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 201, 2):
        #     self.progress.emit(i)
        #     time.sleep(0.00001)
        # for i in range(200, -1, -2):
        #     self.progress.emit(i)
        #     time.sleep(0.00001)
        while True:
            for i in range(0, 501):
                self.progress.emit(i)
                time.sleep(0.01)
            for i in range(500, -1, -1):
                self.progress.emit(i)
                time.sleep(0.01)
        # self.finished.emit()

class Thread3(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(0, 81):
            self.progress.emit(i)
            time.sleep(0.01)
        for i in range(80, -1, -1):
            self.progress.emit(i)
            time.sleep(0.01)
        # while True:
        #     for i in range(0, 81):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(80, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread4(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(0, 51):
            self.progress.emit(i)
            time.sleep(0.01)
        for i in range(50, -1, -1):
            self.progress.emit(i)
            time.sleep(0.01)
        # while True:
        #     for i in range(0, 51):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(50, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread5(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 101):
        #     self.progress.emit(i)
        #     time.sleep(0.001)
        # for i in range(100, -1, -1):
        #     self.progress.emit(i)
        #     time.sleep(0.001)
        # while True:
        #     for i in range(0, 51):
        #         self.progress.emit(i)
        #         time.sleep(0.015)
        #     for i in range(50, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.015)
        # self.finished.emit()

class Thread6(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(0, 51):
            self.progress.emit(i)
            time.sleep(0.01)
        for i in range(50, -1, -1):
            self.progress.emit(i)
            time.sleep(0.01)
        # while True:
        #     for i in range(0, 51):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(50, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread7(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 5):
        #     self.progress.emit(i)
        #     time.sleep(0.01)
        # for i in range(5, -1, -1):
        #     self.progress.emit(i)
        #     time.sleep(0.01)
        # while True:
        #     for i in range(0, 51):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(50, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread8(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(0, 101):
            self.progress.emit(i)
            time.sleep(0.01)
        for i in range(100, -1, -1):
            self.progress.emit(i)
            time.sleep(0.01)
        # while True:
        #     for i in range(0, 101):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(100, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread9(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(0, 101):
            self.progress.emit(i)
            time.sleep(0.01)
        for i in range(100, -1, -1):
            self.progress.emit(i)
            time.sleep(0.01)
        # while True:
        #     for i in range(0, 101):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(100, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread10(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(0, 101):
            self.progress.emit(i)
            time.sleep(0.01)
        for i in range(100, -1, -1):
            self.progress.emit(i)
            time.sleep(0.01)
        # while True:
        #     for i in range(0, 101):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        #     for i in range(100, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.01)
        # self.finished.emit()

class Thread11(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 101):
        #     self.progress.emit(i)
        #     time.sleep(0.01)
        # for i in range(100, -1, -1):
        #     self.progress.emit(i)
        #     time.sleep(0.01)
        # while True:
        #     for i in range(0, 101):
        #         self.progress.emit(i)
        #         time.sleep(0.005)
        #     for i in range(100, -1, -1):
        #         self.progress.emit(i)
        #         time.sleep(0.005)
        # self.finished.emit()