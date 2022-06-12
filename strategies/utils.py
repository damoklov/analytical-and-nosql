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

    def do_some_business_logic(self, data) -> None:
        result = self._strategy.do_algorithm(data)


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data):
        pass
