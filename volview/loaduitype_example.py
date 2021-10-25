"""
PySide example intended to derive a custom class from a widget designed in
QtDesigner, directly from a ui file, without running pyside6-uic.
Just like you could always to in PyQt6:

from PyQt6 import uic


class MySpecializedDesignerWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = uic.loadUi("designed.ui", self)
"""

from PySide6 import QtUiTools, QtWidgets


Ui_Type, UI_Base = QtUiTools.loadUiType("volview.ui")


class MySpecializedDesignerWindow(UI_Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Type()
        self.ui.setupUi(self)


app = QtWidgets.QApplication()
window = MySpecializedDesignerWindow()
window.show()
app.exec()
