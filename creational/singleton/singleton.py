class Singleton:
    __instance = None
    state = 'State 1'
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            Singleton()
        
        return Singleton.__instance
    
    def __init__(self) -> None:
        if self.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.__instance = self
    
    def __str__(self) -> str:
        return self.state

if __name__ == "__main__":
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()
    
    print('Results singleton 1: ', singleton1)
    print('Results singleton 2: ', singleton2)
    
    singleton2.state = 'State 2'
    
    print('Results singleton 1: ', singleton1)
    print('Results singleton 2: ', singleton2)