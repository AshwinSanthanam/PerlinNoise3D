import pygame
import math
from shared_array import SharedArray


class PygameHelper:
    __point_radius = 1

    @classmethod
    def init(cls, width, height):
        cls.__screen = pygame.display.set_mode((width, height))

    @classmethod
    def fill_screen(cls, background=(0, 0, 0)):
        cls.__screen.fill(background)

    @classmethod
    def draw_point(cls, point, color=(255, 255, 255)):
        pygame.draw.circle(cls.__screen, color, point, cls.__point_radius)

    @classmethod
    def update_display(cls):
        pygame.display.flip()

    @classmethod
    def check_for_quit(cls):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()

    @classmethod
    def paint_image(cls, image):
        for x in range(len(image)):
            for y in range(len(image[x])):
                color = image[x][y]
                PygameHelper.draw_point((x, y), (color, color, color))

    @classmethod
    def draw_lines(cls, angles, side):
        for x in range(len(angles)):
            for y in range(len(angles[x])):
                angle = angles[x][y]
                x_center, y_center = (x + 1) * 2 * side, (y + 1) * 2 * side
                x_target, y_target = side * math.cos(angle) + x_center, side * math.sin(angle) + y_center
                pygame.draw.line(cls.__screen, (255, 255, 255), (x_center, y_center), (x_target, y_target))

    @classmethod
    def wait(cls, milli_seconds):
        pygame.time.wait(milli_seconds)

    @classmethod
    def paint_shared_array(cls, shared_array: SharedArray, page: int):
        for y in range(shared_array.y_size):
            for z in range(shared_array.z_size):
                color = shared_array.get(page, y, z)
                PygameHelper.draw_point((y, z), (color, color, color))
