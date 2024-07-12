class Singleton:
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(Singleton):
    def write_log(self, path):
        pass


if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2

