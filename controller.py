from threading import Timer, Lock
from elevator import Elevator
from datetime import datetime as dt


class Controller:
    def __init__(self, elevator=Elevator(10)):
        self.elevator = elevator
        self.state = ''
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
        self.elevator.act()

    def set_state(self, action):
        self.state = \
            {
                'up': 'moving_up',
                'down': 'moving_down',
                'open': 'door_opened',
                'close': 'door_closed',
            }[action.lower()]