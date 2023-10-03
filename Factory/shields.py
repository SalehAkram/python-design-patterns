from Factory.ishield import IShield


class HexShield(IShield):
    def use_shield(self):
        return "using hex shield"


class OvalShield(IShield):
    def use_shield(self):
        return "using oval shield"
