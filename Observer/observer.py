from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def update(self, payload):
        pass


class Saleh(IObserver):
    def update(self, payload):
        print(f"saleh was updated with the following payload {payload}")


class Maryam(IObserver):
    def update(self, payload):
        print(f"Maryam was updated with the following payload {payload}")
