from perlin_noise_generator import PerlinNoiseGenerator, NoiseDimension
from math_helper import Vector
from pygame_helper import PygameHelper
from percentage_calculator import PercentageCalculator
from os import environ

from shared_array import SharedArray

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
vector_set = [Vector(1, 1, 1), Vector(1, -1, 1), Vector(-1, 1, 1), Vector(-1, -1, 1), Vector(1, 1, -1), Vector(1, -1, -1), Vector(-1, 1, -1), Vector(-1, -1, -1)]
shared_array: SharedArray = None
page = 0
page_count = 50
capture = True
percentage_calculator = None


def setup():
    global shared_array
    shared_array = SharedArray(50, 200, 200)
    noise_1 = PerlinNoiseGenerator(NoiseDimension(25, 2), NoiseDimension(200, 1), NoiseDimension(200, 1), vector_set).generate_noise()
    noise_2 = PerlinNoiseGenerator(NoiseDimension(25, 2), NoiseDimension(100, 2), NoiseDimension(100, 2), vector_set).generate_noise()
    noise_3 = PerlinNoiseGenerator(NoiseDimension(25, 2), NoiseDimension(50, 4), NoiseDimension(50, 4), vector_set).generate_noise()
    noise_4 = PerlinNoiseGenerator(NoiseDimension(25, 2), NoiseDimension(25, 8), NoiseDimension(25, 8), vector_set).generate_noise()
    shared_array.add_noise(noise_1, 8)
    shared_array.add_noise(noise_2, 4)
    shared_array.add_noise(noise_3, 2)
    shared_array.add_noise(noise_4, 1)
    shared_array.normalize(0, 255)
    PygameHelper.init(600, 600)


def draw():
    global page
    PygameHelper.fill_screen()
    PygameHelper.paint_shared_array(shared_array, page)
    page += 1
    if capture:
        return page < page_count
    else:
        page %= page_count
        return True


if __name__ == '__main__':
    setup()
    shall_continue = True
    while True:
        if shall_continue:
            shall_continue = draw()
            PygameHelper.update_display()
            if capture:
                PygameHelper.screen_shot(f'out/gif_{page}.png')
        PygameHelper.check_for_quit()
