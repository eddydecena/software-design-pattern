import abc

# base wheeler class
class Wheeler():
    def __init__(self, num_passenger: int) -> None:
        self.num_passenger = num_passenger
    
    def get_price(self):
        pass
    
    def time_estimate(self):
        pass

# type of product
class TwoWheeler(Wheeler):
    def __init__(self, num_passenger: int = 2) -> None:
        super().__init__(num_passenger)

# type of product
class ThreeWheeler(Wheeler):
    def __init__(self, num_passenger: int = 3) -> None:
        super().__init__(num_passenger)

# type of product
class FourWheeler(Wheeler):
    def __init__(self, num_passenger: int = 5) -> None:
        super().__init__(num_passenger)

# Abstract wheeler interface
class IAbstractWheeler(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass) -> bool:
        return (
            hasattr(subclass, 'get_two_wheeler') and
            callable(subclass.get_two_wheeler) and
            hasattr(subclass, 'get_three_wheeler') and
            callable(subclass.get_three_wheeler) and
            hasattr(subclass, 'get_four_wheeler') and
            callable(subclass.get_four_wheeler)
        )

class WheelerFactory(IAbstractWheeler):
    def get_two_wheeler(self) -> object:
        return TwoWheeler()
    
    def get_three_wheeler(self) -> object:
        return ThreeWheeler()
    
    def get_four_wheeler(self) -> object:
        return FourWheeler()

if __name__ == '__main__':
    wheeler_factory = WheelerFactory()
    two_wheeler = wheeler_factory.get_two_wheeler()
    three_wheeler = wheeler_factory.get_three_wheeler()
    four_wheeler = wheeler_factory.get_four_wheeler()
