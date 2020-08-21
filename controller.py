from threading import Timer, Lock
from elevator import Elevator
from datetime import datetime as dt


class Controller:
    def __init__(self, elevator=Elevator(10)):
        self.elevator = elevator
        self._state = ''
        self.elevator.subscribe(self.set_state)
        self.lock = Lock()

    def call(self, floor, datetime):
        seconds = (datetime - dt.now()).total_seconds()
        Timer(seconds,  self.command, [self.elevator.call, floor]).start()

    def select(self, floor, datetime):
        seconds = (datetime-dt.now()).total_seconds()
        Timer(seconds, self.command, [self.elevator.select, floor]).start()

    def command(self, fct, arg):
        with self.lock:
            fct(arg)

    def set_state(self, action):
        self._state = \
            {
                'up': 'moving_up',
                'down': 'moving_down',
                'open': 'door_opened',
                'close': 'door_closed',
            }[action.lower()]

    def get_state(self):
        return self.state
