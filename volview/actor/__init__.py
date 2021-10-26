from abc import ABC, abstractmethod


class GLActor(ABC):
    @abstractmethod
    def init_gl(self) -> None:
        pass

    @abstractmethod
    def draw_gl(self) -> None:
        pass

    @abstractmethod
    def dispose_gl(self) -> None:
        pass
