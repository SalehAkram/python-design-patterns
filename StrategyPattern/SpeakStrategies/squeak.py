from StrategyPattern.SpeakStrategies.ispeak_strategy import ISpeakStrategy


class Squeak(ISpeakStrategy):
    def speak(self):
        return "Squak Squak"
