import math
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class SliceWidget(QtWidgets.QWidget):
    """
    Canvas widget showing 2D slice of volume rendering stuff.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eye_image = QtGui.QPixmap("EyeIcon2.png")
        self.scaled_eye = self.eye_image.scaledToWidth(
            self.eye_image.width() // 2,
            Qt.SmoothTransformation,
        )
        self.setMouseTracking(True)  # enable hover for mouseMoveEvent
        self.angle = 0

    def _eye_xy(self):
        x = self.width() / 2
        y = self.height() - 40
        return x, y

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        x = event.pos().x()
        y = event.pos().y()
        ex, ey = self._eye_xy()
        dx = x - ex
        dy = ey - y
        self.angle = math.degrees(math.atan2(dx, dy))
        # print(self.angle)
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent):
        # print("paintEvent")
        super().paintEvent(event)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        x, y = self._eye_xy()
        painter.translate(x, y)
        img = self.scaled_eye
        x = -img.width() / 2
        y = -img.height() / 2
        painter.rotate(self.angle)
        # view ray
        pen = QtGui.QPen(Qt.green)
        pen.setStyle(Qt.DashLine)
        pen.setWidth(2)
        pen.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 0, 100)))
        painter.setPen(pen)
        painter.drawLine(0, 0, 0, -(self.height() + self.width()))
        # picture of eye
        painter.translate(x, y)
        painter.drawPixmap(0, 0, img)
