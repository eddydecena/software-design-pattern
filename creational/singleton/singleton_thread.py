import threading

class Singleton:
    __lock = threading.Lock()
    __instance = None
    state = 'State 1'

    @classmethod
    def get_instance(cls):
        if not Singleton.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()
        
        return cls.__instance
    
    def __str__(self) -> str:
        return self.state

if __name__ == "__main__":
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()
    
    print('Results Singleton 1: ', singleton1)
    print('Results Singleton 2: ', singleton2)
    
    singleton2.state = 'State 2'
    
    print('Results Singleton 1: ', singleton1)
    print('Results Singleton 2: ', singleton2)