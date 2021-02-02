from typing import Dict

class ComplexCar():
    def __init__(self, name: str, car_type: str) -> None:
        self.name = name
    
    def print_info(self) -> None:
        print(f'Complex {self.name}')

class Car():
    _cars: Dict[str, object] = {}
    
    def __init__(self, name: str, car_type: str) -> None:
        self._complex_car = ComplexCar(name, car_type)
    
    def __new__(cls, name: str, car_type: str) -> object:
        try:
            car = cls._cars[name]
        except KeyError:
            car = object.__new__(Car)
            cls._cars[name] = car
        
        return car

    def __repr__(self) -> str:
        return f"This is a {self._complex_car.name} {self._complex_car.name}"

if __name__ == '__main__':
    print(Car('Audi', 'A9'), Car('Toyota', 'Corola'), Car('Tesla', 'Cybertrunk'), Car('Tesla', 'model x'))
    print(len(Car._cars))
    print(Car('Tesla', 'model x') is Car('Tesla', 'Cybertrunk'))