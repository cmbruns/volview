"""
Test modular window type
"""

# Pluggable renderers
from volview.actor.hello_triangle import HelloTriangle

# Pluggable window systems
from volview.window.glfw_window import GlfwWindow
from volview.window.qt_window import SimpleQtWindow

with SimpleQtWindow(renderer=HelloTriangle()) as window:
    window.render_loop()
