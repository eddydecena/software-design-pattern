from abc import ABCMeta
from abc import abstractmethod

class IImage(metaclass=ABCMeta):
    _filename: str
    
    @abstractmethod
    def load_image_from_disk(self) -> None:
        pass
    
    @abstractmethod
    def display_image(self) -> None:
        pass

class Image(IImage):
    def __init__(self, filename: str) -> None:
        self._filename = filename
    
    def load_image_from_disk(self) -> None:
        print(f'Loading from {self._filename}')
    
    def display_image(self) -> None:
        print(f'display {self._filename}')

class Proxy():
    def __init__(self, subject: Image) -> None:
        self._subject = subject
        self._proxystate = None
    
    def display_image(self) -> None:
        if self._proxystate == None:
            self._subject.load_image_from_disk()
            self._proxystate = 1
        self._subject.display_image()

if __name__ == '__main__':
    proxy = Proxy(Image('myphoto.jpg'))
    proxy.display_image()