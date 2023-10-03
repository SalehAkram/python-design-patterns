from abc import ABC, abstractmethod


class IWeapon(ABC):

    @abstractmethod
    def use_weapon(self):
        pass
