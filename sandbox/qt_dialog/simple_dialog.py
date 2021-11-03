from PySide6 import QtGui, QtWidgets


class TestWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCentralWidget(QtWidgets.QPushButton("Hey!"))

    def paintEvent(self, event):
        print("paint")
        super().paintEvent(event)
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.end()


app = QtWidgets.QApplication()
window1 = TestWindow()
window1.show()
app.exec()
