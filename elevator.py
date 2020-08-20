class Elevator:
    def __init__(self, n, current=0):
        self.n = n
        self.called = [False] * self.n
        self.selected = [False] * self.n
        self.current = current
        self.opened = False  # Can't move if the door is opened
        self.actions = []

    def check(self, floor):
        if floor < 0 or floor >= self.n:
            raise Exception('The chosen level is not valid')

    def select(self, floor):
        self.check(floor)
        self.selected[floor] = True
        self.plan(self.selected)

    def call(self, floor):
        self.check(floor)
        self.called[floor] = True
        self.plan(self.called)

    def plan(self, selection):
        self.actions = []
        current = self.current
        current = self.plan_up(selection, current, range(self.current, self.n))
        if self.current > 0:
            self.plan_down(selection, current, range(self.current, -1, -1))

    def plan_up(self, selection, current, floors):
        for floor in floors:
            if selection[floor]:
                steps = floor - current
                self.actions = self.actions + ['up' for _ in range(0, steps)] + ['open', 'close']
                current = floor
        return current

    def plan_down(self, selection, current, floors):
        for floor in floors:
            if selection[floor]:
                steps = current - floor
                self.actions = self.actions + ['down' for _ in range(0, steps)] + ['open', 'close']
                current = floor
        return current

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
