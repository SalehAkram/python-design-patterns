from StrategyPattern.dog import Dog
from StrategyPattern.eagle import Eagle

animals = [Dog(), Eagle()]

for a in animals:
    print(a.display())
    print(a.speak())
    print(a.fly())
