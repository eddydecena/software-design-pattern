from abc import ABCMeta
from abc import abstractmethod

class IGraphic(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass: object) -> bool:
        return (
            hasattr(subclass, 'print') and
            callable(subclass.print)
        )

class Quadratic(IGraphic):
    def print(self):
        print('I am a Quadratic!')

class Cycle(IGraphic):
    def print(self):
        print('I am a Cycle!')

class GraphicComponent():
    def __init__(self):
        self.graphics = []
    
    def add(self, graphic: IGraphic):
        self.graphics.append(graphic)
    
    def print(self):
        for g in self.graphics:
            g.print()

    def remove(self, graphic: IGraphic):
        self.graphics.remove(graphic)


if __name__ == "__main__":
    q1 = Quadratic()
    c1 = Cycle()
    
    q2 = Quadratic()
    c2 = Cycle()
    
    gc1 = GraphicComponent()
    gc2 = GraphicComponent()
    
    gc1.add(c1)
    gc2.add(q1)
    gc1.add(q2)
    gc2.add(c2)
    gc2.add(q2)
    gc2.add(gc1)
    
    gc2.print()