import sys
from OpenGL import GL
from PySide6 import QtGui, QtOpenGL, QtWidgets
from volview.actor import GLActor
from volview.window import GLWindow


class QtGLWindow(QtOpenGL.QOpenGLWindow):
    def __init__(self, renderer: GLActor):
        super().__init__()
        self.renderer = renderer

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """Cleans up openGL resources before the app exits"""
        self.makeCurrent()
        self.renderer.dispose_gl()
        self.doneCurrent()

    def initializeGL(self) -> None:
        self.renderer.init_gl()

    def paintGL(self) -> None:
        self.renderer.draw_gl()

    def resizeGL(self, width: int, height: int) -> None:
        self.makeCurrent()
        GL.glViewport(0, 0, width, height)
        self.doneCurrent()
        self.update()


class SimpleQtWindow(GLWindow):
    def __init__(self, renderer: GLActor):
        super().__init__()
        self.renderer = renderer

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def render_loop(self):
        """Window will dispose of the renderer [unless it's a shared context?]"""
        app = QtWidgets.QApplication(sys.argv)
        window = QtGLWindow(self.renderer)
        window.show()
        app.exec()  # GL context will be destroyed before this returns...
