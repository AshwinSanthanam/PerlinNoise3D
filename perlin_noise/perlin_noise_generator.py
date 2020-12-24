import random
from multiprocessing import Value
from math_helper import Vector, interpolate, fade


class NoiseDimension:
    def __init__(self, noise_length: int, grid_length: int):
        self.__noise_length = noise_length
        self.__grid_length = grid_length

    @property
    def noise_length(self) -> int:
        return self.__noise_length

    @property
    def grid_length(self) -> int:
        return self.__grid_length

    @property
    def range(self) -> int:
        return self.__grid_length * self.__noise_length

    def compute_local_position(self, global_position) -> float:
        return (global_position % self.__noise_length) / (self.__noise_length - 1)

    def compute_grid_vector_position(self, global_position) -> int:
        return global_position // self.__noise_length


class PerlinNoiseGenerator:
    def __init__(self, x_dim: NoiseDimension, y_dim: NoiseDimension, z_dim: NoiseDimension, vector_set: list[Vector]):
        self.__x_dim = x_dim
        self.__y_dim = y_dim
        self.__z_dim = z_dim
        self.__vector_set = vector_set

    def generate_noise(self) -> list[list[list[float]]]:
        noise = self.__init_noise()
        grid_vectors = self.__generate_grid_vectors()
        unit_size_y = 50
        unit_size_z = 50
        process_count_y = self.__y_dim.range // unit_size_y
        process_count_z = self.__z_dim.range // unit_size_z
        for x in range(self.__x_dim.range):
            dist_x = self.__x_dim.compute_local_position(x)
            grid_x = self.__x_dim.compute_grid_vector_position(x)
            fade_x = fade(dist_x)
            for y_unit in range(process_count_y):
                y_offset = y_unit * unit_size_y
                y_remaining = self.__y_dim.range - y_offset
                y_len = unit_size_y if y_remaining >= unit_size_y else y_remaining
                for z_unit in range(process_count_z):
                    z_offset = z_unit * unit_size_z
                    z_remaining = self.__z_dim.range - z_offset
                    z_len = unit_size_z if z_remaining >= unit_size_z else z_remaining
                    self.__generate_unit_noise(grid_vectors, x, grid_x, dist_x, fade_x, noise, y_offset, y_len, z_offset, z_len)
        return noise

    def __generate_unit_noise(self, grid_vectors, x, grid_x, dist_x, fade_x, noise, y_offset, y_len, z_offset, z_len):
        for y in range(y_offset, y_offset + y_len):
            dist_y = self.__y_dim.compute_local_position(y)
            grid_y = self.__y_dim.compute_grid_vector_position(y)
            fade_y = fade(dist_y)
            for z in range(z_offset, z_offset + z_len):
                dist_z = self.__z_dim.compute_local_position(z)
                grid_z = self.__z_dim.compute_grid_vector_position(z)
                fade_z = fade(dist_z)

                lu_d = grid_vectors[grid_x][grid_y][grid_z] * Vector(dist_x, dist_y, dist_z)
                ru_d = grid_vectors[grid_x + 1][grid_y][grid_z] * Vector(dist_x - 1, dist_y, dist_z)
                ld_d = grid_vectors[grid_x][grid_y + 1][grid_z] * Vector(dist_x, dist_y - 1, dist_z)
                rd_d = grid_vectors[grid_x + 1][grid_y + 1][grid_z] * Vector(dist_x - 1, dist_y - 1, dist_z)
                lu_u = grid_vectors[grid_x][grid_y][grid_z + 1] * Vector(dist_x, dist_y, dist_z - 1)
                ru_u = grid_vectors[grid_x + 1][grid_y][grid_z + 1] * Vector(dist_x - 1, dist_y, dist_z - 1)
                ld_u = grid_vectors[grid_x][grid_y + 1][grid_z + 1] * Vector(dist_x, dist_y - 1, dist_z - 1)
                rd_u = grid_vectors[grid_x + 1][grid_y + 1][grid_z + 1] * Vector(dist_x - 1, dist_y - 1, dist_z - 1)

                u_d = interpolate(lu_d, ru_d, fade_x)
                d_d = interpolate(ld_d, rd_d, fade_x)
                u_u = interpolate(lu_u, ru_u, fade_x)
                d_u = interpolate(ld_u, rd_u, fade_x)
                d = interpolate(u_d, d_d, fade_y)
                u = interpolate(u_u, d_u, fade_y)
                z_interpolated = interpolate(d, u, fade_z)
                noise[x][y][z] = z_interpolated

    def __generate_grid_vectors(self) -> list[list[list[Vector]]]:
        grid_vectors = []
        for x in range(self.__x_dim.grid_length):
            grid_plane = []
            for y in range(self.__y_dim.grid_length + 1):
                grid_line = []
                for z in range(self.__z_dim.grid_length + 1):
                    grid_line.append(self.__get_random_vector())
                grid_plane.append(grid_line)
            grid_vectors.append(grid_plane)
        grid_vectors.append(grid_vectors[0])
        return grid_vectors

    def __get_random_vector(self) -> Vector:
        return self.__vector_set[random.randint(0, len(self.__vector_set) - 1)]

    def __init_noise(self) -> list[list[list[float]]]:
        noise_cube = []
        for x in range(self.__x_dim.range):
            noise_plane = []
            for y in range(self.__y_dim.range):
                noise_line = []
                for z in range(self.__z_dim.range):
                    noise_line.append(0)
                noise_plane.append(noise_line)
            noise_cube.append(noise_plane)
        return noise_cube
