from abc import ABCMeta, abstractmethod

class IEuropeanSocket(metaclass=ABCMeta):
    @abstractmethod
    def voltage(self) -> int:
        pass

    @abstractmethod
    def live(self) -> int:
        pass
    
    @abstractmethod
    def neutral(self) -> int:
        pass
    
    @abstractmethod
    def earth(self) -> int:
        pass

class Socket(IEuropeanSocket):
    def voltage(self) -> int:
        return 230

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1

    def earch(self) -> int:
        return 0

class IUSASocket(metaclass=ABCMeta):
    @abstractmethod
    def voltage(self) -> int:
        pass

    @abstractmethod
    def live(self) -> int:
        pass

    @abstractmethod
    def neutral(self) -> int:
        pass

class Adapter(IUSASocket):
    def __init__(self, socket: object) -> None:
        self.__socket = socket
    def voltage(self) -> int:
        return 110

    def live(self) -> int:
        return self.__socket.live()

    def neutral(self) -> int:
        return self.__socket.neutral()

if __name__ == '__main__':
    socket = Socket()
    adapter = Adapter(socket)
