# i_plane.py

import abc


class IPlane(abc.ABC):
    @abc.abstractmethod
    def update(self) -> None: ...

    @abc.abstractmethod
    def draw(self) -> None: ...

    @abc.abstractmethod
    def move_left(self) -> None: ...

    @abc.abstractmethod
    def move_right(self) -> None: ...
