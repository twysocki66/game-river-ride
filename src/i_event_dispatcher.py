# i_event_dispatcher.py

import abc


class IEventDispatcher(abc.ABC):
    @abc.abstractmethod
    def add_handler(self, event_type: int, event_key: int, handler_fun) -> None: ...

    @abc.abstractmethod
    def loop(self) -> None: ...
