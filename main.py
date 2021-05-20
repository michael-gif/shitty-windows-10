import pygame

from config import *
from widgets import *

# classes and functions here

pygame.init()

def get_res_tuple():
    minimum = (800, 600)
    infoObject = pygame.display.Info()
    maximum = (infoObject.current_w, infoObject.current_h)
    res = [int(a) for a in config.get('resolution')['value'].split('x')]
    # check if the resolution is bound by a minimum
    if config.get('resolution')['minimum']:
        if res[0] < minimum[0] or res[1] < minimum[1]:
            print('Configured resolution less than allowed minimum, failed to boot')
            raise Exception
    if config.get('resolution')['maximum']:
        if res[0] > maximum[0] or res[1] > maximum[1]:
            print('Configured resolution more than allowed minimum, failed to boot')
            raise Exception
    return res

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
