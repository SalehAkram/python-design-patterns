from abc import ABC, abstractmethod


class IShield(ABC):

    @abstractmethod
    def use_shield(self):
        pass
