from Factory.iweapon import IWeapon


class Spear(IWeapon):
    def use_weapon(self):
        return "Using Spear"


class Sword(IWeapon):
    def use_weapon(self):
        return "Using Sword"
