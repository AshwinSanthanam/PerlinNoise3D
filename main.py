from perlin_noise.min_max_normalizer import MinMaxNormalizer
from perlin_noise.perlin_noise_generator import PerlinNoiseGenerator
from perlin_noise.vector import Vector
from pygame_helper import PygameHelper

vector_set = [Vector(1, 1, 1), Vector(1, -1, 1), Vector(-1, 1, 1), Vector(-1, -1, 1), Vector(1, 1, -1), Vector(1, -1, -1), Vector(-1, 1, -1), Vector(-1, -1, -1)]
page = 0
noise_size = 200
grid_size = 2
noise_height = 10
grid_height = 2
normalized_noise = None


def setup():
    global normalized_noise
    noise = PerlinNoiseGenerator(noise_size, grid_size, noise_height, grid_height, vector_set).generate_noise()
    normalized_noise = MinMaxNormalizer(noise, 255).normalize()
    PygameHelper.init(800, 800)


def draw():
    global page
    PygameHelper.fill_screen()
    PygameHelper.paint_image(normalized_noise[page])
    page += 1
    page %= noise_height * grid_height
    return True


if __name__ == '__main__':
    setup()
    shall_continue = True
    while True:
        if shall_continue:
            shall_continue = draw()
            PygameHelper.update_display()
        PygameHelper.check_for_quit()
