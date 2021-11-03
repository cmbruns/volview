"""
The volview.window module generalizes the source
of OpenGL contexts to provide a common API for Qt
and glfw windows.
"""

from abc import ABC, abstractmethod


class GLWindow(ABC):
    @abstractmethod
    def render_loop(self):
        pass
