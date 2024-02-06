# i_background.py

import abc


class IBackground(abc.ABC):
    @abc.abstractmethod
    def update(self) -> None: ...

    @abc.abstractmethod
    def speed_inc(self) -> None: ...

    @abc.abstractmethod
    def speed_dec(self) -> None: ...


class IBackgroundLayer(abc.ABC):
    @abc.abstractmethod
    def update(self) -> None: ...
