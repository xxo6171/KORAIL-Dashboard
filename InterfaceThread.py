from PySide2.QtCore import QThread, Signal

class Threads:
    def __init__(self):
        self.t1 = Thread1(); self.t2 = Thread2(); self.t3 = Thread3()
        self.t4 = Thread4(); self.t5 = Thread5(); self.t6 = Thread6()
        self.t7 = Thread7(); self.t8 = Thread8(); self.t9 = Thread9()
        self.t10 = Thread10(); self.t11 = Thread11()

    def getThreadList(self):
        return [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6,
                self.t7, self.t8, self.t9, self.t10, self.t11]

class Thread1(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 8):
        #     self.progress.emit(i)
        #     time.sleep(0.01)
        # for i in range(80, -1, -1):
        #     self.progress.emit(i)
        #     time.sleep(0.01)

        # while True:
        #     for i in range(0, 9):
        #         self.progress.emit(i)
        #         self.msleep(1)
        #     for i in range(8, -1, -1):
        #         self.progress.emit(i)
        #         self.msleep(1)
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
        # while True:
        #     for i in range(0, 261):
        #         self.progress.emit(i)
        #         self.msleep(1)
        #     for i in range(260, -1, -1):
        #         self.progress.emit(i)
        #         self.msleep(1)
        # self.finished.emit()

class Thread3(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 81):
        #     self.progress.emit(i)
        #     self.msleep(16)
        # for i in range(80, -1, -1):
        #     self.progress.emit(i)
        #     self.msleep(16)
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
        pass
        # for i in range(0, 51):
        #     self.progress.emit(i)
        #     self.msleep(1)
        # for i in range(50, -1, -1):
        #     self.progress.emit(i)
        #     self.msleep(1)
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
        #     for i in range(0, 101):
        #         self.progress.emit(i)
        #         self.msleep(20)
        #     for i in range(100, -1, -1):
        #         self.progress.emit(i)
        #         self.msleep(20)
        # self.finished.emit()

class Thread6(QThread):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        pass
        # for i in range(0, 51):
        #     self.progress.emit(i)
        #     self.msleep(1)
        # for i in range(50, -1, -1):
        #     self.progress.emit(i)
        #     self.msleep(1)
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
        pass
        # for i in range(0, 101):
        #     self.progress.emit(i)
        #     self.msleep(1)
        # for i in range(100, -1, -1):
        #     self.progress.emit(i)
        #     self.msleep(1)
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
        pass
        # for i in range(0, 101):
        #     self.progress.emit(i)
        #     self.msleep(1)
        # for i in range(100, -1, -1):
        #     self.progress.emit(i)
        #     self.msleep(1)
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
        pass
        # for i in range(0, 101):
        #     self.progress.emit(i)
        #     self.msleep(1)
        # for i in range(100, -1, -1):
        #     self.progress.emit(i)
        #     self.msleep(1)
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
        #         self.msleep(1)
        #     for i in range(100, -1, -1):
        #         self.progress.emit(i)
        #         self.msleep(1)
        # self.finished.emit()