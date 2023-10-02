from abc import ABC, abstractmethod


class ISpeakStrategy(ABC):
    @abstractmethod
    def speak(self):
        pass
