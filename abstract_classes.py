from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self):
        self.max_speed = 0
        self.current_speed = 0

    @abstractmethod
    def move(self, speed):
        pass

class VW(Vehicle):

    def move(self, speed):
        self.current_speed = speed

