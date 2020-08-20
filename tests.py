import unittest
from elevator import Elevator, Direction


class ElevatorTests(unittest.TestCase):
    def test_goto(self):
        elevator = Elevator(10)
        level = 3
        elevator.goto(level)
        self.assertEqual(elevator.current + 1, level)
        self.assertEqual(elevator.direction, Direction.Still)


if __name__ == '__main__':
    unittest.main()
