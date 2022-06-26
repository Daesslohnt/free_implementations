class Singletone(type): #metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singletone, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singletone):

    def log(self, msg):
        print(msg)

logger1 = Logger()
logger2 = Logger()

print(logger2 == logger1)