from typing import Optional

from abc import ABC, ABCMeta
from abc import abstractmethod

class AbstractHandler(metaclass=ABCMeta):
    def __init__(self, next_handle: object) -> None:
        self._next = next_handle
    
    def handle(self, request: str) -> None:
        handled = self.process_request(request)
        
        if not handled:
            self._next.handle(request)
    
    @abstractmethod
    def process_request(request: str) -> Optional[bool]:
        raise NotImplementedError('Not implement, you should implement it first.')

class FirstHandler(AbstractHandler):
    def process_request(self, request: str) -> Optional[bool]:
        if 'a' < request <= 'e': 
            print("This is {} handling request '{}'".format(self.__class__.__name__, request)) 
            return True

class SecondHandler(AbstractHandler):
    def process_request(self, request: str) -> Optional[bool]:
        if 'e' < request <= 'l': 
            print("This is {} handling request '{}'".format(self.__class__.__name__, request)) 
            return True

class ThirdHandler(AbstractHandler):
    def process_request(self, request: str) -> Optional[bool]:
        if 'l' < request <= 'z': 
            print("This is {} handling request '{}'".format(self.__class__.__name__, request)) 
            return True

class DefaultHandler(AbstractHandler):
    def process_request(self, request: str) -> Optional[bool]:
        print("This is {} handling request '{}'".format(self.__class__.__name__, request)) 
        return True

if __name__ == '__main__':
    handler =  FirstHandler(SecondHandler(ThirdHandler(DefaultHandler(None))))
    
    word = str(input('An word to handle: '))
    
    for letter in word:
        handler.handle(letter)
