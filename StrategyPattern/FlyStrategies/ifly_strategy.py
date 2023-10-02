from abc import ABC, abstractmethod


class IFlyStrategy(ABC):
    @abstractmethod
    def fly(self):
        pass
