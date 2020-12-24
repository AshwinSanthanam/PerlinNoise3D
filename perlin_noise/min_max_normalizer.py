from shared_array import SharedArray


class MinMaxNormalizer:
    def __init__(self, noise: SharedArray, scale: float):
        self.__noise = noise
        self.__scale = scale

    def normalize(self):
        max_value = self.__get_max()
        min_value = self.__get_min()
        normalized_noise = []
        for plane in self.__noise:
            normalized_plane = []
            for row in plane:
                normalized_row = []
                for value in row:
                    normalized_value = int(self.__scale * (value - min_value) / (max_value - min_value))
                    normalized_row.append(normalized_value)
                normalized_plane.append(normalized_row)
            normalized_noise.append(normalized_plane)
        return normalized_noise

    def __get_min(self):
        min_val = self.__noise[0][0][0]
        for x in range(self.__noise.x_size):
            for y in range(self.__noise.y_size):
                for z in range(self.__noise.z_size):
                    value = self.__noise.get()
                    min_val = value if min_val > value else min_val
        return min_val

    def __get_max(self):
        max_val = self.__noise[0][0][0]
        for plane in self.__noise:
            for row in plane:
                for value in row:
                    max_val = value if max_val < value else max_val
        return max_val
