from abc import ABC, abstractmethod

from volview.actor import GLActor


class GLWindow(ABC):
    @abstractmethod
    def render_loop(self):
        pass
