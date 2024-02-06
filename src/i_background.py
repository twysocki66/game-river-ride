# i_background.py

import abc


class IBackground(abc.ABC):
    @abc.abstractmethod
    def update(self) -> None: ...


class IBackgroundLayer(abc.ABC):
    @abc.abstractmethod
    def update(self) -> None: ...
