from StateMachine.States.istate import IState
from StateMachine.States.no_card import NoCard


class PinValidated(IState):
    def __init__(self, sm):
        self.state_machine = sm

    def insert_card(self):
        return "card already inserted"

    def enter_pin(self):
        return "Cant enter pin, pin already entered and validated"

    def dispense_cash(self):
        return "Dispensing $500"

    def eject_card(self):
        self.state_machine.update_state(NoCard(self.state_machine))
        return "Card ejecting"
