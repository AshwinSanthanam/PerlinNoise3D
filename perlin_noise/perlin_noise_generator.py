import random
from perlin_noise.vector import Vector


class PerlinNoiseGenerator:
    def __init__(self, noise_size, grid_size, vector_set):
        self.__noise_size = noise_size
        self.__grid_size = grid_size
        self.__vector_set = vector_set

    def generate_noise(self):
        grid_vectors = self.__generate_grid_vectors()
        noise = PerlinNoiseGenerator.__init_noise(self.__noise_size * self.__grid_size)
        for grid_x in range(self.__grid_size):
            for grid_y in range(self.__grid_size):
                for grid_z in range(self.__grid_size):
                    self.__generate_unit_noise(noise, grid_vectors, grid_x, grid_y, grid_z)
        return noise

    def __generate_unit_noise(self, noise, grid_vectors, grid_x, grid_y, grid_z):
        max_len = self.__noise_size - 1
        for x in range(self.__noise_size):
            x_dist = x / max_len
            for y in range(self.__noise_size):
                y_dist = y / max_len
                for z in range(self.__noise_size):
                    z_dist = z / max_len
                    lu_d = grid_vectors[grid_x][grid_y][grid_z] * Vector(x_dist, y_dist, z_dist)
                    ru_d = grid_vectors[grid_x + 1][grid_y][grid_z] * Vector(x_dist - 1, y_dist, z_dist)
                    ld_d = grid_vectors[grid_x][grid_y + 1][grid_z] * Vector(x_dist, y_dist - 1, z_dist)
                    rd_d = grid_vectors[grid_x + 1][grid_y + 1][grid_z] * Vector(x_dist - 1, y_dist - 1, z_dist)
                    lu_u = grid_vectors[grid_x][grid_y][grid_z + 1] * Vector(x_dist, y_dist, z_dist - 1)
                    ru_u = grid_vectors[grid_x + 1][grid_y][grid_z + 1] * Vector(x_dist - 1, y_dist, z_dist - 1)
                    ld_u = grid_vectors[grid_x][grid_y + 1][grid_z + 1] * Vector(x_dist, y_dist - 1, z_dist - 1)
                    rd_u = grid_vectors[grid_x + 1][grid_y + 1][grid_z + 1] * Vector(x_dist - 1, y_dist - 1, z_dist - 1)

                    fade_x = self.__fade(x_dist)
                    fade_y = self.__fade(y_dist)
                    fade_z = self.__fade(z_dist)
                    u_d = self.__interpolate(lu_d, ru_d, fade_x)
                    d_d = self.__interpolate(ld_d, rd_d, fade_x)
                    u_u = self.__interpolate(lu_u, ru_u, fade_x)
                    d_u = self.__interpolate(ld_u, rd_u, fade_x)
                    d = self.__interpolate(u_d, d_d, fade_y)
                    u = self.__interpolate(u_u, d_u, fade_y)
                    z_interpolated = self.__interpolate(d, u, fade_z)
                    x_offset = self.__noise_size * grid_x
                    y_offset = self.__noise_size * grid_y
                    z_offset = self.__noise_size * grid_z
                    noise[x_offset + x][y_offset + y][z_offset + z] = z_interpolated

    @classmethod
    def __interpolate(cls, lower_lim, upper_lim, pos):
        return lower_lim + pos * (upper_lim - lower_lim)

    @classmethod
    def __fade(cls, dist):
        return 6 * (dist ** 5) - 15 * (dist ** 4) + 10 * (dist ** 3)

    def __generate_grid_vectors(self):
        grid_vectors = []
        for x in range(self.__grid_size):
            grid_plane = []
            for y in range(self.__grid_size + 1):
                grid_line = []
                for z in range(self.__grid_size + 1):
                    grid_line.append(self.__get_random_vector())
                grid_plane.append(grid_line)
            grid_vectors.append(grid_plane)
        grid_vectors.append(grid_vectors[0])
        return grid_vectors

    def __get_random_vector(self):
        return self.__vector_set[random.randint(0, len(self.__vector_set) - 1)]

    @staticmethod
    def __init_noise(side):
        noise_cube = []
        for x in range(side):
            noise_plane = []
            for y in range(side):
                noise_line = []
                for z in range(side):
                    noise_line.append(0)
                noise_plane.append(noise_line)
            noise_cube.append(noise_plane)
        return noise_cube
