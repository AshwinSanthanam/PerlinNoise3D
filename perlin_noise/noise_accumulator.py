class NoiseAccumulator:
    def __init__(self, noise_size, grid_size):
        self.__noise_size = noise_size
        self.__grid_size = grid_size
        self.__grid_x = 0
        self.__grid_y = 0
        self.__grid_z = 0
        self.noise = self.__init_noise(noise_size, grid_size)

    def set_noise_value(self, x, y, z, noise_value):
        x_offset = self.__noise_size * self.__grid_x
        y_offset = self.__noise_size * self.__grid_y
        z_offset = self.__noise_size * self.__grid_z
        self.noise[x_offset + x][y_offset + y][z_offset + z] = noise_value

    def move_to_next_grid(self):
        self.__grid_z += 1
        if self.__grid_z == self.__grid_size:
            self.__grid_z = 0
            self.__grid_y += 1
            if self.__grid_y == self.__grid_size:
                self.__grid_y = 0
                self.__grid_x += 1

    @staticmethod
    def __init_noise(noise_size, grid_size):
        noise_cube = []
        for x in range(noise_size * grid_size):
            noise_plane = []
            for y in range(noise_size * grid_size):
                noise_line = []
                for z in range(noise_size * grid_size):
                    noise_line.append(0)
                noise_plane.append(noise_line)
            noise_cube.append(noise_plane)
        return noise_cube
