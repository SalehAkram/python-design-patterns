from StrategyPattern.dog import Dog
from StrategyPattern.eagle import Eagle
from StateMachine.state_machine import StateMachine
# animals = [Dog(), Eagle()]
#
# for a in animals:
#     print(a.display())
#     print(a.speak())
#     print(a.fly())

state_machine = StateMachine()
machine_on = True

while machine_on:
    choice = input("I: Insert Card, P: Enter Pin, D: Dispense Cash. E: Eject Card\n")
    if choice.lower() == "x":
        machine_on = False
    elif choice.lower() == "i":
        print(choice)
        state_machine.insert_card()
    elif choice.lower() == "p":
        state_machine.enter_pin()
    elif choice.lower() == "d":
        state_machine.dispense_cash()
    elif choice.lower() == "e":
        state_machine.eject_card()


