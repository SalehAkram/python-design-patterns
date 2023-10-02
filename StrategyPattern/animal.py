from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, fly_strategy, speak_strategy):
        self.fly_strategy = fly_strategy
        self.speak_strategy = speak_strategy

    def fly(self):
        return self.fly_strategy.fly()

    def speak(self):
        return self.speak_strategy.speak()

    @abstractmethod
    def display(self):
        pass

