from StrategyPattern.dog import Dog
from StrategyPattern.eagle import Eagle
from StateMachine.state_machine import StateMachine
# animals = [Dog(), Eagle()]
#
# for a in animals:
#     print(a.display())
#     print(a.speak())
#     print(a.fly())

# state_machine = StateMachine()
# machine_on = True
#
# while machine_on:
#     choice = input("I: Insert Card, P: Enter Pin, D: Dispense Cash. E: Eject Card\n")
#     if choice.lower() == "x":
#         machine_on = False
#     elif choice.lower() == "i":
#         print(choice)
#         state_machine.insert_card()
#     elif choice.lower() == "p":
#         state_machine.enter_pin()
#     elif choice.lower() == "d":
#         state_machine.dispense_cash()
#     elif choice.lower() == "e":
#         state_machine.eject_card()

from Factory.gladiators import GladiatorFactory
choice = input("m or r\n").lower()
g_factory = GladiatorFactory().get_factory(choice)

weapon = g_factory.create_weapon()
shield = g_factory.create_shield()

print(weapon.use_weapon())
print(shield.use_shield())



