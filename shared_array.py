from multiprocessing import Array


class SharedArray:
    def __init__(self, x_size: int, y_size: int, z_size: int):
        self.__x_size = x_size
        self.__y_size = y_size
        self.__z_size = z_size
        self.__array = Array('f', x_size * y_size * z_size)

    @property
    def x_size(self):
        return self.__x_size

    @property
    def y_size(self):
        return self.__y_size

    @property
    def z_size(self):
        return self.__z_size

    def set(self, x: int, y: int, z: int, value: float):
        target_index = self.__compute_index(x, y, z)
        self.__array[target_index] = value

    def get(self, x: int, y: int, z: int):
        target_index = self.__compute_index(x, y, z)
        return self.__array[target_index]

    def normalize(self, lower_limit, upper_limit):
        scale = upper_limit - lower_limit
        min_val = min(self.__array)
        max_val = max(self.__array)
        array_range = max_val - min_val
        for i in range(len(self.__array)):
            self.__array[i] = lower_limit + scale * ((self.__array[i] - min_val) / array_range)

    def __compute_index(self, x: int, y: int, z: int):
        return x * self.__y_size * self.__z_size + y * self.__z_size + z
