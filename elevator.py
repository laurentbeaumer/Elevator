class Elevator:
    def __init__(self, n, current=0):
        self.n = n
        self.selected = [False] * self.n
        self.current = current
        self.opened = False  # Can't move if the door is opened
        self.actions = []

    def select(self, floor):
        if floor < 0 or floor >= self.n:
            raise Exception('The chosen level is not valid')

        self.selected[floor] = True

    def plan(self):

        current = self.current
        for floor in range(self.current, self.n):
            if self.selected[floor]:
                steps = floor - current
                self.actions = self.actions + ['up' for _ in range(0, steps)] + ['open', 'close']
                current = floor

        if self.current > 0:
            for floor in range(self.current, -1, -1):
                if self.selected[floor]:
                    steps = current - floor
                    self.actions = self.actions + ['down' for _ in range(0, steps)] + ['open', 'close']
                    current = floor

    def up(self):
        if self.opened:
            raise Exception('Door is not closed, elevator cannot move')

        self.current += 1

    def down(self):
        if self.opened:
            raise Exception('Door is not closed, elevator cannot move')

        self.current -= 1

    def open(self):
        self.opened = True
        self.selected[self.current] = False

    def close(self):
        self.opened = False

    def act(self):
        for action in self.actions:
            {
                'up': self.up,
                'down': self.down,
                'open': self.open,
                'close': self.close,
            }[action.lower()]()
        self.actions = []
