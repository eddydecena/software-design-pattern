from abc import ABC
from abc import abstractmethod

class Receiver():
    def execute(self):
        print('Doing something!!')

class ICommand(ABC):
    _receiver: Receiver
    
    @abstractmethod
    def process(self) -> None:
        pass

class Command(ICommand):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver = receiver
    
    def process(self) -> None:
        self._receiver.execute()

class Invoker():
    @classmethod
    def command(self, cmd: Command):
        self._cmd = cmd
    
    @classmethod
    def execute(self):
        self._cmd.process()

if __name__ == '__main__':
    receiver = Receiver()
    cmd = Command(receiver)
    Invoker.command(cmd)
    Invoker.execute()
