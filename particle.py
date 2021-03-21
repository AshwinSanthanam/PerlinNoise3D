class Particle:
    __angles: [int] = [0, 45, 90, 135, 180, 225, 270, 315]
    __displacement = {
        0: (1, 0),
        45: (1, 1),
        90: (0, 1),
        135: (-1, 1),
        180: (-1, 0),
        225: (-1, -1),
        270: (0, -1),
        315: (1, -1)
    }

    def __init__(self, x: int, y: int, z: int):
        self.__x = x
        self.__y = y
        self.__z = z

    def move(self, direction: float):
        diff = 0
        new_direction = 0
        for angle in Particle.__angles:
            new_diff = abs(direction - angle)
            if diff > new_diff:
                diff = new_diff
                new_direction = angle
        displacement = Particle.__displacement[new_direction]
        self.__y += displacement[0]
        self.__z += displacement[1]