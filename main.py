import math

import pygame as pg

W_WIDTH, W_HEIGHT = 1280, 720
FPS = 60


class Planet(pg.sprite.Sprite):

    def __init__(self, image_path, d_angle, scale, arbyte_radius, d_alpha):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (100 * scale, 100 * scale))

        self.default_image = self.image.copy()

        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

        self.center = self.rect.center

        self.d_angle = d_angle

        self.arbyte_radius = arbyte_radius
        self.d_alpha = d_alpha

        self.major_planet = None

    def rotate_of_planet(self, angle, arbyte_center):
        offset = pg.Vector2(
            0,
            self.arbyte_radius
        )

        offset = offset.rotate(angle)

        return self.image, self.image.get_rect(center=arbyte_center + offset)

    def rotate_of_yourself(self, angle):
        image_rotated = pg.transform.rotate(self.default_image, angle)
        rect_rotated = image_rotated.get_rect(center=self.center)

        return image_rotated, rect_rotated

    def update(self, tick):
        current_angle = (self.d_angle * tick) * math.pi / 180
        current_alpha = (self.d_alpha * tick) * math.pi / 180

        current_center = self.major_planet.rect.center

        self.image, self.rect = self.rotate_of_yourself(current_angle)
        self.image, self.rect = self.rotate_of_planet(current_alpha, current_center)


pg.init()

screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()

sun = Planet("./images/sun.png", -1, 1.5, 0, 0)
sun.major_planet = sun

mercury = Planet("./images/sun.png", -100, 0.5, 80, 400)
mercury.major_planet = sun

venus = Planet("./images/sun.png", -100, 0.8, 120, 300)
venus.major_planet = sun

earth = Planet("./images/sun.png", -100, 1, 200, 200)
earth.major_planet = sun

moon = Planet("./images/sun.png", -100, 0.2, 100, 400)
moon.major_planet = earth

sub_moon = Planet("./images/sun.png", -100, 0.2, 30, 1500)
sub_moon.major_planet = moon

all_sprites = pg.sprite.Group()
all_sprites.add([mercury, venus, earth, moon, sun, sub_moon])

is_running = True

tick = 0
while is_running:
    clock.tick(FPS)
    tick += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    all_sprites.update(tick=tick)

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)
    pg.display.flip()
