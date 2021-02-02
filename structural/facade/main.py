from abc import ABC, ABCMeta
from abc import abstractmethod

class IActivity(metaclass=ABCMeta):
    @abstractmethod
    def make(self) -> None:
        pass

class Washing(IActivity):
    def make(self) -> None:
        print('Washing...')

class Rinsing(IActivity):
    def make(self) -> None:
        print('Rinsing...')

class Spinning(IActivity):
    def make(self) -> None:
        print('Spinning...')

class IWashingMachine(metaclass=ABCMeta):
    _washing: Washing
    _rinsing: Rinsing
    _spinning: Spinning
    
    @abstractmethod
    def wash(self) -> None:
        pass

class WashingMachine(IWashingMachine):
    def __init__(self):
        self._washing = Washing()
        self._rinsing = Rinsing()
        self._spinning = Spinning()

    def wash(self) -> None:
        self._washing.make()
        self._rinsing.make()
        self._spinning.make()

if __name__ == '__main__':
    wm = WashingMachine()
    wm.wash()