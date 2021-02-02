class Borg:
    __share_state: dict = dict()
    
    def __init__(self) -> None:
        self.__dict__ = self.__share_state
        self.state = 'State 1'
    
    def __str__(self) -> str:
        return self.state

if __name__ == "__main__":
    borg1 = Borg()
    borg2 = Borg()
    
    print('Result borg 1: ', borg1)
    print('Result borg 2: ', borg2)
    
    borg2.state = 'State 2'
    
    print('Result borg 1: ', borg1)
    print('Result borg 2: ', borg2)