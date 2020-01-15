import random
from CP1404.prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        r = random.randint(1, 100)
        if r >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven