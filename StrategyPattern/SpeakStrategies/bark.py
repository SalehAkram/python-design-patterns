from StrategyPattern.SpeakStrategies.ispeak_strategy import ISpeakStrategy


class Bark(ISpeakStrategy):
    def speak(self):
        return "Woof Woof"
