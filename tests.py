import unittest
from elevator import Elevator


class ElevatorTests(unittest.TestCase):
    def test_invalid_selected_floor(self):
        elevator = Elevator(5)
        floor = 5
        with self.assertRaises(Exception):
            elevator.select(floor)

    def test_select_up(self):
        elevator = Elevator(10)
        floor = 3
        elevator.select(floor)
        elevator.plan()
        elevator.act()
        self.assertEqual(elevator.current, floor)

    def test_select_down(self):
        elevator = Elevator(10, 5)
        floor = 2
        elevator.select(floor)
        elevator.plan()
        elevator.act()
        self.assertEqual(elevator.current, floor)

    def test_multiple_select_up(self):
        elevator = Elevator(10)
        elevator.select(1)
        elevator.select(3)
        elevator.select(6)
        elevator.select(8)
        elevator.plan()
        elevator.act()
        self.assertEqual(elevator.current, 8)

    def test_multiple_select_down(self):
        elevator = Elevator(10, 8)
        elevator.select(5)
        elevator.select(2)
        elevator.select(0)
        elevator.plan()
        elevator.act()
        self.assertEqual(elevator.current, 0)

    def test_unordered_select(self):
        elevator = Elevator(10, 4)
        elevator.select(5)
        elevator.select(2)
        elevator.select(0)
        elevator.select(8)
        elevator.select(7)
        elevator.plan()
        elevator.act()
        self.assertEqual(elevator.current, 0)


if __name__ == '__main__':
    unittest.main()
