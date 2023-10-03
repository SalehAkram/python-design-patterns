from Factory.igladiator_factory import IGladiatorFactory
from Factory.ishield import IShield
from Factory.iweapon import IWeapon
from Factory.shields import OvalShield, HexShield
from Factory.weapons import Sword, Spear


class MurmilloFactory(IGladiatorFactory):
    def create_weapon(self) -> IWeapon:
        return Sword()

    def create_shield(self) -> IShield:
        return OvalShield()


class RetiariusFactory(IGladiatorFactory):
    def create_weapon(self) -> IWeapon:
        return Spear()

    def create_shield(self) -> IShield:
        return HexShield()


class GladiatorFactory:
    def __init__(self):
        self.factory_dic = {
            "m": MurmilloFactory(),
            "r": RetiariusFactory()
        }

    def get_factory(self, key) -> IGladiatorFactory:
        return self.factory_dic[key]
