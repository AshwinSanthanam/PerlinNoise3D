from perlin_noise.min_max_normalizer import MinMaxNormalizer
from perlin_noise.perlin_noise_generator import PerlinNoiseGenerator
from perlin_noise.vector import Vector
from pygame_helper import PygameHelper

vector_set = [Vector(1, 1, 1), Vector(1, -1, 1), Vector(-1, 1, 1), Vector(-1, -1, 1), Vector(1, 1, -1), Vector(1, -1, -1), Vector(-1, 1, -1), Vector(-1, -1, -1)]
normalized_noise = None
page = 0
noise_size = 50
grid_size = 4


def setup():
    global normalized_noise
    noise = PerlinNoiseGenerator(noise_size, grid_size, vector_set).generate_noise()
    normalized_noise = MinMaxNormalizer(noise, 255).normalize()
    PygameHelper.init(800, 800)


def draw():
    global page
    PygameHelper.paint_image(normalized_noise[page])
    page += 1
    page %= grid_size * noise_size
    return True


if __name__ == '__main__':
    setup()
    shall_continue = True
    while True:
        if shall_continue:
            shall_continue = draw()
            PygameHelper.update_display()
        PygameHelper.check_for_quit()
