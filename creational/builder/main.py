import builtins
from typing import Union

from abc import ABCMeta, abstractmethod

# Product
class Course():
    def __init__(self, kind: str, fee: Union[int, float] = 100, batches: int = 5) -> None:
        self.kind = kind
        self.fee = fee
        self.batches = batches
    
    def __str__(self) -> str:
        return f"Type: {self.kind} - Fee: {self.fee.value} - Batches: {self.batches.value}"

# Builder interface
class ICourseBulder(metaclass=ABCMeta):
    @classmethod
    def __subclasshok__(cls, subclass: object) -> bool:
        return (
            hasattr(subclass, 'fee') and
            hasattr(subclass, 'available_batches') and
            callable(subclass.available_batches)
        )

    @abstractmethod
    def get_fee(self) -> Union[int, float]:
        pass
    
    @abstractmethod
    def get_batches(self) -> int:
        pass

# Online Course builder
class OnlineCourseBuilder(ICourseBulder):
    def get_kind(self) -> str:
        return 'online'
    
    def get_fee(self) -> Union[int, float]:
        fee = Fee()
        fee.value = 5
        return fee
    
    def get_batches(self) -> int:
        batches = Batches()
        batches.value = 100
        return batches

# Part of the course
class Fee():
    value: int

class Batches():
    value: int

class Director():
    def __init__(self, builder: ICourseBulder) -> None:
        self.__builder = builder
    
    def construct(self) -> Course:
        course = Course(kind=self.__builder.get_kind(),
                        fee=self.__builder.get_fee(),
                        batches=self.__builder.get_batches())
        return course

if __name__ == "__main__":
    builder = OnlineCourseBuilder()
    director = Director(builder=builder)
    course = director.construct()
    print(course)