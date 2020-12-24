class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __mul__(self, other):
        return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __neg__(self):
        return Vector(-self.__x, -self.__y, -self.__z)

    def __str__(self):
        return f"(x: {self.__x}, y: {self.__y}, z: {self.__z})"
