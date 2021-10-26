from abc import ABC, abstractmethod


class GLWindow(ABC):
    @abstractmethod
    def render_loop(self):
        pass
