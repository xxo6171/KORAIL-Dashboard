from qtpy.QtCore import QObject, Signal, QEvent

# 오브젝트 클릭 함수
def clickable(widget):
    class Filter(QObject):
        # clicked = pyqtSignal()
        clicked = Signal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonPress:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked