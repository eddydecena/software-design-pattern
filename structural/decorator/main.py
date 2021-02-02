from abc import ABC, ABCMeta
from abc import abstractmethod

class IWrittenText(metaclass=ABCMeta):
    text: str
    
    @abstractmethod
    def render(self) -> str:
        pass

class WrittenText(IWrittenText):
    def __init__(self, text: str):
        self._text = text
    
    def render(self) -> str:
        return self._text

class UnderlineWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    
    def render(self) -> str:
        return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    
    def render(self) -> str:
        return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    
    def render(self) -> str:
        return "<b>{}</b>".format(self._wrapped.render())

if __name__ == '__main__':
    print(BoldWrapper(ItalicWrapper(UnderlineWrapper(WrittenText('Hello Decorator!')))).render())