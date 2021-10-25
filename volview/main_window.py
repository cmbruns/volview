from PySide6 import QtUiTools

Ui_VolView, VolViewBase = QtUiTools.loadUiType("volview.ui")


class VolViewWindow(VolViewBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_VolView()
        self.ui.setupUi(self)


__all__ = [
    "VolViewWindow",
]
