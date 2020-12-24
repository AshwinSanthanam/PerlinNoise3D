class NoiseFragment:
    def __init__(self, x_offset: int, y_offset: int, z_offset: int, noise: list[list[float]]):
        self.__x_offset = x_offset
        self.__y_offset = y_offset
        self.__z_offset = z_offset
        self.__noise = noise

    @property
    def x_offset(self):
        return self.__x_offset

    @property
    def y_offset(self):
        return self.__y_offset

    @property
    def z_offset(self):
        return self.__z_offset

    @property
    def noise(self):
        return self.__noise
