from StateMachine.States.istate import IState
from StateMachine.States.pin_validated import PinValidated


class CardInserted(IState):
    def __init__(self, sm):
        self.state_machine = sm

    def insert_card(self):
        return "card already inserted"

    def enter_pin(self):
        self.state_machine.update_state(PinValidated(self.state_machine))
        return "Pin entered and is correct"

    def dispense_cash(self):
        return "Cant dispense cash: without a entering a valid pin"

    def eject_card(self):
        self.state_machine.update_state(NoCard(self.state_machine))
        return "Card ejecting"


from StateMachine.States.no_card import NoCard