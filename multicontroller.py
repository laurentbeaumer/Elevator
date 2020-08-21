from controller import Controller
from elevator import Elevator


class MultiController:
    def __init__(self, num_elevators,  num_floors):
        if num_floors < 1:
            raise Exception('You need at least one elevator')

        self.n = num_elevators
        self.controllers = []
        for i in range(0, num_elevators):
            self.controllers.append(Controller(Elevator(num_floors)))

    def call(self, floor, datetime):
        ctrl = self.controllers[0]
        min_diff = abs(floor - ctrl.elevator.current)

        for controller in self.controllers:
            diff = abs(floor - controller.elevator.current)
            if diff == 0:
                ctrl = controller
                break
            elif diff < min_diff:
                ctrl = controller
        ctrl.call(floor, datetime)
        return ctrl
