from abc import ABCMeta
from abc import abstractmethod

class ICreatingAPI(metaclass=ABCMeta):
    @abstractmethod
    def create(self, length: int, breadth: int, height: int) ->  None:
        pass
    
    def __subclasshook__ (self, subclass) -> bool:
        return (
            hasattr(subclass, 'create') and
            callable(subclass.create)
        )

class CreatingAPI1(ICreatingAPI):
    def create(self, length: int, breadth: int, height: int) ->  None:
        print(f'API1 is producing Cuboid with length = {length}, '
                f' Breadth = {breadth} and Height = {height}')

class CreatingAPI2(ICreatingAPI):
    def create(self, length: int, breadth: int, height: int) ->  None:
        print(f'API2 is producing Cuboid with length = {length}, '
                f' Breadth = {breadth} and Height = {height}')

class ICuboid(metaclass=ABCMeta):
    _length: int
    _breadth: int
    _height: int
    _creatingAPI: ICreatingAPI
    
    @abstractmethod
    def produce(self) -> None:
        pass
    
    @abstractmethod
    def expand(self, times: int) -> None:
        pass
    
    def __subclasshook__ (self, subclass) -> bool:
        return (
            hasattr(subclass, 'produce') and
            callable(subclass.produce) and
            hasattr(subclass, 'expand') and
            callable(subclass.expand) and
            hasattr(subclass, '_length') and
            hasattr(subclass, '_breadth') and
            hasattr(subclass, '_height') and
            hasattr(subclass, '_producingAPI')
        )

class Cuboid(ICuboid):
    def __init__(self, length: int, breadth: int, height: int, creatingAPI: ICreatingAPI) -> None:
        super().__init__()
        
        self._length = length
        self._breadth = breadth
        self._height = height
        
        self._creatingAPI = creatingAPI

    def produce(self) -> None:
        self._creatingAPI.create(self._length, self._breadth, self._height)
    
    def expand(self, times: int) -> None:
        self._length *= times
        self._breadth *= times
        self._height *= times

cuboid1 = Cuboid(1, 2, 3, CreatingAPI1()) 
cuboid1.produce()

cuboid2 = Cuboid(19, 19, 19, CreatingAPI2()) 
cuboid2.produce()