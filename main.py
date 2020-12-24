from perlin_noise.min_max_normalizer import MinMaxNormalizer
from perlin_noise.perlin_noise_generator import PerlinNoiseGenerator, NoiseDimension
from perlin_noise.vector import Vector
from pygame_helper import PygameHelper

vector_set = [Vector(1, 1, 1), Vector(1, -1, 1), Vector(-1, 1, 1), Vector(-1, -1, 1), Vector(1, 1, -1), Vector(1, -1, -1), Vector(-1, 1, -1), Vector(-1, -1, -1)]
page = 0
x_dim = NoiseDimension(10, 5)
y_dim = NoiseDimension(50, 2)
z_dim = NoiseDimension(50, 2)
normalized_noise = None


def setup():
    global normalized_noise
    noise = PerlinNoiseGenerator(x_dim, y_dim, z_dim, vector_set).generate_noise()
    normalized_noise = MinMaxNormalizer(noise, 255).normalize()
    PygameHelper.init(800, 800)


def draw():
    global page
    PygameHelper.fill_screen()
    PygameHelper.paint_image(normalized_noise[page])
    page += 1
    page %= x_dim.range
    return True


if __name__ == '__main__':
    setup()
    shall_continue = True
    while True:
        if shall_continue:
            shall_continue = draw()
            PygameHelper.update_display()
        PygameHelper.check_for_quit()
