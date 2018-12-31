import pygame
from pygame import *
from sys import exit

pygame.init()
background_img = "timg.jpg"
mouse_background = "logo17.png"
screen = pygame.display.set_mode((2560, 1440), FULLSCREEN, 32)
pygame.display.set_caption("hello")
background = pygame.image.load(background_img).convert()
mouse_cursor = pygame.image.load(mouse_background).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    x, y = pygame.mouse.get_pos()
    print("pos", x, y)
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    #print("get", x, y)
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()
    # 刷新一下画面
