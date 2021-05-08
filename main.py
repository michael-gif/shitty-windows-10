import pygame

from config import *
from widgets import *

# classes and functions here

pygame.init()

config = Config()

def get_res_tuple():
    temp = config.get('resolution')
    return (int(temp.split('x')[0]), int(temp.split('x')[1]))

screen = pygame.display.set_mode(get_res_tuple())
pygame.display.set_caption('Windows 10')
clock = pygame.time.Clock()

background = Background(screen)
taskbar = TaskBar(screen)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    mouse_pos = pygame.mouse.get_pos()
    mouse_state = pygame.mouse.get_pressed()

    background.render(mouse_pos, mouse_state)
    taskbar.render(mouse_pos, mouse_state)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
