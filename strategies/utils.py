from __future__ import annotations
from abc import ABC, abstractmethod


class Context:

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self, filename, data) -> None:
        self._strategy.do_algorithm(filename, data)


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, filename, data):
        pass
