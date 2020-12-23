import pygame


class PygameHelper:
    __point_radius = 1

    @classmethod
    def init(cls, width, height):
        cls.__screen = pygame.display.set_mode((width, height))

    @classmethod
    def fill_screen(cls, background=(0, 0, 0)):
        cls.__screen.fill(background)

    @classmethod
    def draw_line(cls, p1, p2, color=(255, 255, 255)):
        pygame.draw.line(cls.__screen, color, p1, p2)

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
