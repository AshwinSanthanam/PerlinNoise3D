import math
import random

from math_helper import Vector


class FlowField:
    __directions = [0, 45, 90, 135, 180, 225, 270, 315, 360]

    def __init__(self, noise, number_of_particals):
        self.__noise = noise
        self.__particals = self.__init_particals(number_of_particals, len(noise))

    def move(self):
        for partical in self.__particals:
            direction = self.__noise[partical.x][partical.y] * 180 / math.pi
            new_direction = FlowField.__find_closest_dir()

    @staticmethod
    def __find_closest_dir(old_direction):
        new_direction = 0
        min_difference = 360
        for direction in FlowField.__directions:
            current_difference = abs(direction - old_direction)
            if current_difference < min_difference:
                current_difference = min_difference
                new_direction = direction
        return new_direction

    @staticmethod
    def __init_particals(number_of_particals, distance):
        particals = []
        for i in range(number_of_particals):
            x = random.randint(0, distance - 1)
            y = random.randint(0, distance - 1)
            particals.append(Vector(x, y))
        return particals
