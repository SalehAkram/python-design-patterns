from abc import ABC, abstractmethod

class ISoldier(ABC):

    @abstractmethod
    def rush_forward(self):
        pass

    @abstractmethod
    def step_back(self):
        pass

    @abstractmethod
    def attack(self):
        pass



