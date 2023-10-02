from abc import ABC, abstractmethod


class IState(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def dispense_cash(self):
        pass

    @abstractmethod
    def eject_card(self):
        pass
