from enum import Enum


class Direction(Enum):
    Up = 1
    Still = 0
    Down = -1


class Elevator:
    def __init__(self, n):
        self.n = n
        self.levels = [False] * self.n
        self.current = 0
        self.opened = False  # Can't move if the door is opened
        self.direction = Direction.Still
        self.actions = []

    def goto(self, level):
        if level <= 0 or level > self.n:
            raise Exception('The chosen level is not valid')

        self.levels[level] = True
        steps = level - self.current
        direction = Direction[steps % 1]

        if self.Direction == direction:
            act = ['move' for i in steps] + ['open', 'close']

    def move(self):
        if self.opened:
            raise Exception('Door is not closed, elevator cannot move')

        if self.direction == Direction.Still:
            raise Exception('There is no direction for the elevator to move')

        self.current += self.direction.value

    def open(self):
        self.opened = True
        self.levels[self.current] = False

    def close(self):
        self.opened = False

    def act(self):
        for action in self.actions:
            {
                'move': self.move,
                'open': self.open,
                'close': self.open,
                'move': self.open,
            }[action]()
