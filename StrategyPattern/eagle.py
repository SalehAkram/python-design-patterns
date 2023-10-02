from StrategyPattern.animal import Animal
from StrategyPattern.FlyStrategies.high_altitude import HighAltitude
from StrategyPattern.SpeakStrategies.squeak import Squeak


class Eagle(Animal):
    def __init__(self):
        super().__init__(HighAltitude(), Squeak())

    def display(self):
        return "I am an Eagle"
