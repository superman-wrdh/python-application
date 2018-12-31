background_image_filename = 'img.png'
sprite_image_filename = 'logo17.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((2560, 1440), FULLSCREEN, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# Clock对象
clock = pygame.time.Clock()

x = 0.
# 速度（像素/秒）
speed = 250.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    # 想一下，这里减去640和直接归零有何不同？
    if x > 1000.:
        x -= 1000.

    pygame.display.update()
