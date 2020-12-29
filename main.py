from perlin_noise_generator import PerlinNoiseGenerator, NoiseDimension
from math_helper import Vector
from pygame_helper import PygameHelper
from percentage_calculator import PercentageCalculator
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
vector_set = [Vector(1, 1, 1), Vector(1, -1, 1), Vector(-1, 1, 1), Vector(-1, -1, 1), Vector(1, 1, -1), Vector(1, -1, -1), Vector(-1, 1, -1), Vector(-1, -1, -1)]
x_dim = NoiseDimension(25, 2)
y_dim = NoiseDimension(50, 2)
z_dim = NoiseDimension(50, 2)
shared_array = None
page = 0
percentage_calculator = None


def setup():
    global shared_array
    shared_array = PerlinNoiseGenerator(x_dim, y_dim, z_dim, vector_set).generate_noise()
    PygameHelper.init(y_dim.range, z_dim.range)


def draw():
    global page
    PygameHelper.fill_screen()
    PygameHelper.paint_shared_array(shared_array, page)
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
            # PygameHelper.screen_shot(f'out/gif_{page}.png')
        PygameHelper.check_for_quit()
