from Adapter.irobot import IRobot
from Adapter.isoldier import ISoldier


class Rambo(ISoldier):
    def rush_forward(self):
        print("Rambo running")

    def step_back(self):
        print("Rambo retreating")

    def attack(self):
        print("Rambo firing AK47")

class Robocop(IRobot):

    def advance(self):
        print("Robocop advancing: Your move creep")

    def jump(self):
        print("Robocop jumping")

    def fire_weapon(self):
        print("Robocop firing his gun")


class SoldierRobotAdapter(ISoldier):
    def __init__(self, irobot):
        self.robot = irobot

    def rush_forward(self):
        self.robot.advance()

    def step_back(self):
        self.robot.jump()

    def attack(self):
        self.robot.fire_weapon()
