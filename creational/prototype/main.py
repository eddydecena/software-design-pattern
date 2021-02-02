import copy
from abc import ABCMeta
from abc import abstractmethod

# Prototype Interface
class ICourse(metaclass=ABCMeta):
    _id: int = None
    _type: str = None
    
    @abstractmethod
    def clone(self):
        pass
    
    def get_type(self):
        return self._type
    
    def get_id(self) -> int:
        return self._id
    
    def set_id(self, id: int) -> None:
        self._id = id

# SDE Course
class SDE(ICourse):
    def __init__(self) -> None:
        super(ICourse, self).__init__()
        self._type = 'SDE'
    
    @classmethod
    def clone(cls):
        return copy.copy(cls)

# DSA Course
class DSA(ICourse):
    def __init__(self) -> None:
        super(ICourse, self).__init__()
        self._type = 'DSA'
    
    @classmethod
    def clone(cls):
        return copy.copy(cls)

# STL
class STL(ICourse):
    def __init__(self) -> None:
        super(ICourse, self).__init__()
        self._type = 'STL'
    
    @classmethod
    def clone(cls):
        return copy.copy(cls)

# Static Factory
class CourseFactory():
    __cache = {}
    
    def initialize():
        #
        sde = SDE()
        sde.set_id(1)
        CourseFactory.__cache[1] = sde
        
        #
        dsa = DSA()
        dsa.set_id(2)
        CourseFactory.__cache[2] = dsa
        
        #
        stl = STL()
        stl.set_id(3)
        CourseFactory.__cache[3] = stl
    
    def get_by_id(id):
        return CourseFactory.__cache[id]

if __name__ == "__main__":
    CourseFactory.initialize()
    
    for id in range(1, 4):
        print(f'Course instance: {CourseFactory.get_by_id(id)}')