import threading
from elevator import Elevator


class Controller:
    def __init__(self, elevator = Elevator(10)):
        self.elevator = elevator
        self._state = elevator.state
        self.elevator.subscribe(self.set_state)

    def command(self, action, timespan):
        threading.Timer(timespan, self.elevator.action.append(action)).start()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self.state
