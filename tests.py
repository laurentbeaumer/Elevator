import unittest
from elevator import Elevator


class ElevatorTests(unittest.TestCase):
    def test_goto(self):
        elevator = Elevator(10)
        level = 3
        elevator.goto(level)
        self.assertEqual(elevator.current + 1, level)


if __name__ == '__main__':
    unittest.main()
