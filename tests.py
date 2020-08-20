import unittest
from elevator import Elevator, Direction


class ElevatorTests(unittest.TestCase):
    def test_goto(self):
        elevator = Elevator(10)
        floor = 3
        elevator.select(floor)
        self.assertEqual(elevator.current + 1, floor)
        self.assertEqual(elevator.direction, Direction.Still)


if __name__ == '__main__':
    unittest.main()
