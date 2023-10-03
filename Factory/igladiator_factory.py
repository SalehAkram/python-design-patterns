from abc import ABC, abstractmethod

from Factory.ishield import IShield
from Factory.iweapon import IWeapon


class IGladiatorFactory(ABC):

    @abstractmethod
    def create_weapon(self) -> IWeapon:
        pass

    @abstractmethod
    def create_shield(self) -> IShield:
        pass
