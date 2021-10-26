"""
"""

from volview.actor.hello_triangle import HelloTriangle
from volview.window.glfw_window import GlfwWindow
from volview.window.qt_window import SimpleQtWindow

with GlfwWindow(renderer=HelloTriangle()) as window:
    window.render_loop()
