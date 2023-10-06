from abc import ABC, abstractmethod

class IRobot(ABC):

    @abstractmethod
    def advance(self):
        pass

    @abstractmethod
    def jump(self):
        pass

    @abstractmethod
    def fire_weapon(self):
        pass



