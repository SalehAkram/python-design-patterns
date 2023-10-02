from StateMachine.States.istate import IState


class NoCard(IState):
    def __init__(self, sm):
        self.state_machine = sm

    def insert_card(self):
        self.state_machine.update_state(CardInserted(self.state_machine))
        return "card inserted"

    def enter_pin(self):
        return "Cant Enter pin: there are no cards inserted: insert card first"

    def dispense_cash(self):
        return "Cant dispense cash: no card has been inserted: Insert card first"

    def eject_card(self):
        return "Cant eject card: no card has been inserted: Insert card first"


from StateMachine.States.card_inserted import CardInserted
