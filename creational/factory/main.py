class TwoWheeler():
    def __init__(self, num_passenger: int=2) -> None:
        self.num_passenger = num_passenger
    
    def get_price(self):
        pass
    
    def time_estimate(self):
        pass

class ThreeWheeler():
    def __init__(self, num_passenger: int=3) -> None:
        self.num_passenger = num_passenger
    
    def get_price(self):
        pass
    
    def time_estimate(self):
        pass

class FourWheeler():
    def __init__(self, num_passenger=5) -> None:
        self.num_passenger = num_passenger
    
    def get_price(self):
        pass
    
    def time_estimate(self):
        pass

def WheelerFactory(name: str='FourWheeler', num_passenger=None) -> object:
    factories = {
        'TwoWheeler': TwoWheeler() if not num_passenger else TwoWheeler(num_passenger),
        'ThreeWheeler': ThreeWheeler() if not num_passenger else ThreeWheeler(num_passenger),
        'FourWheeler': FourWheeler() if not num_passenger else FourWheeler() 
    }
    
    return factories[name]

if __name__ == '__main__':
    four_wheeler = WheelerFactory()
