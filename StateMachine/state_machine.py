from StateMachine.States.no_card import NoCard


class StateMachine:
    def __init__(self):
        self.current_state = NoCard(self)

    def update_state(self, state):
        self.current_state = state

    def insert_card(self):
        print(self.current_state.insert_card())

    def enter_pin(self):
        print(self.current_state.enter_pin())

    def dispense_cash(self):
        print(self.current_state.dispense_cash())

    def eject_card(self):
        print(self.current_state.eject_card())


