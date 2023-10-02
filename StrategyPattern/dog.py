from StrategyPattern.animal import Animal
from StrategyPattern.FlyStrategies.cant_fly import CantFly
from StrategyPattern.SpeakStrategies.bark import Bark


class Dog(Animal):
    def __init__(self):
        super().__init__(CantFly(), Bark())

    def display(self):
        return "I am a dog"
