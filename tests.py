import unittest
import datetime as dt
import logging
from logging import info
from time import sleep
from controller import Controller
from elevator import Elevator
logging.basicConfig(level=logging.ERROR)


class ElevatorTests(unittest.TestCase):
    def test_invalid_selected_floor(self):
        info("Test: {0}".format("test_invalid_selected_floor"))
        elevator = Elevator(5)
        floor = 5
        with self.assertRaises(Exception):
            elevator.select(floor)

    def test_select_up(self):
        info("Test: {0}".format("test_select_up"))
        elevator = Elevator(10)
        floor = 3
        elevator.select(floor)
        elevator.act()
        self.assertEqual(elevator.current, floor)

    def test_select_down(self):
        info("Test: {0}".format("test_select_down"))
        elevator = Elevator(10, 5)
        floor = 2
        elevator.select(floor)
        elevator.act()
        self.assertEqual(elevator.current, floor)

    def test_multiple_select_up(self):
        info("Test: {0}".format("test_multiple_select_up"))
        elevator = Elevator(10)
        elevator.select(1)
        elevator.select(3)
        elevator.select(6)
        elevator.select(8)
        elevator.act()
        self.assertEqual(elevator.current, 8)

    def test_multiple_select_down(self):
        info("Test: {0}".format("test_multiple_select_down"))
        elevator = Elevator(10, 8)
        elevator.select(5)
        elevator.select(2)
        elevator.select(0)
        elevator.act()
        self.assertEqual(elevator.current, 0)

    def test_unordered_select(self):
        info("Test: {0}".format("test_unordered_select"))
        elevator = Elevator(10, 4)
        elevator.select(5)
        elevator.select(2)
        elevator.select(0)
        elevator.select(8)
        elevator.select(7)
        elevator.act()
        self.assertEqual(elevator.current, 0)

    def test_call_and_select(self):
        info("Test: {0}".format("test_call_and_select"))
        elevator = Elevator(10, 4)
        from_floor = 2
        to_floor = 6
        elevator.call(from_floor)
        elevator.act()
        elevator.select(to_floor)
        elevator.act()
        self.assertEqual(elevator.current, to_floor)

    def test_multiple_call_and_multiple_select(self):
        info("Test: {0}".format("test_multiple_call_and_multiple_select"))
        elevator = Elevator(10, 4)
        elevator.call(1)
        elevator.call(3)
        elevator.call(5)
        elevator.act()
        self.assertEqual(elevator.current, 1)

        elevator.select(2)
        elevator.select(5)
        elevator.select(3)
        elevator.act()
        self.assertEqual(elevator.current, 5)

    def test_controller_delayed_command(self):
        info("Test: {0}".format("test_controller_delayed_command"))
        elevator = Elevator(10, 2)
        controller = Controller(elevator)
        controller.select(3, dt.datetime.now() + dt.timedelta(0, 1))
        sleep(2)
        self.assertEqual(elevator.current, 3)
        self.assertEqual(controller.state, 'door_closed')


if __name__ == '__main__':
    unittest.main()
