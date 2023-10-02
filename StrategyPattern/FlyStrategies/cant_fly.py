from ifly_strategy import IFlyStrategy


class CantFly(IFlyStrategy):
    def fly(self):
        return "Can't fly to save my life"
