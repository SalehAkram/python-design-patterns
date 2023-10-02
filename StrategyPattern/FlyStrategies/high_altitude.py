from StrategyPattern.FlyStrategies.ifly_strategy import IFlyStrategy


class HighAltitude(IFlyStrategy):
    def fly(self):
        return "Flying High!!!"
