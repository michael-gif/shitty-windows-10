import pygame

from config import *

config = Config()

class Widget:
    def __init__(self, screen, pos, width, height):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height

class Button(Widget):
    def __init__(self, screen, pos, snap, width, height, src, src_hover, src_click):
        super().__init__(screen, pos, width, height)
        self.snap = snap
        self.src = f'./resources/buttons/{src}'
        self.src_hover = f'./resources/buttons/{src_hover}'
        self.src_click = f'./resources/buttons/{src_click}'
        self.image = pygame.image.load(self.src).convert_alpha()
        self.image_hover = pygame.image.load(self.src_hover).convert_alpha()
        self.image_click = pygame.image.load(self.src_click).convert_alpha()

    def render(self, mouse_pos, mouse_state):
        screen_size = self.screen.get_size()
        if self.snap != False:
            # snap the x component
            x = self.pos[0]
            y = self.pos[1]
            if 'n' in self.snap:
                y = 0
            if 's' in self.snap:
                y = screen_size[1] - self.height
            if 'e' in self.snap:
                x = screen_size[0] - self.width
            if 'w' in self.snap:
                x = 0
            self.pos = (x, y)
        
        # clicking the button
        if self.mouse_over(mouse_pos) and mouse_state[0]:
            self.screen.blit(self.image_click, self.pos)
        # hovering over the button
        elif self.mouse_over(mouse_pos):
            self.screen.blit(self.image_hover, self.pos)
        # not hovering over the button
        else:
            self.screen.blit(self.image, self.pos)

    # check if the mouse is over the button, depending on the button's position, width and height
    def mouse_over(self, mouse_pos):
        return mouse_pos[0] >= self.pos[0] and mouse_pos[0] <= self.pos[0] + self.width and mouse_pos[1] >= self.pos[1] and mouse_pos[1] <= self.pos[1] + self.height

class Background(Widget):
    def __init__(self, screen):
        res = config.get('resolution')
        super().__init__(screen, (0, 0), int(res.split('x')[0]), int(res.split('x')[1]))
        self.image_path = f'./resources/background/{config.get("resolution")}.jpg'
        self.image_surface = pygame.image.load(self.image_path).convert_alpha()

    def render(self, mouse_pos, mouse_state):
        self.screen.blit(self.image_surface, self.pos)

class TaskBar(Widget):
    def __init__(self, screen):
        super().__init__(screen, (0, 0), 100, 100)
        config = Config()
        self.image_path = f'./resources/taskbar/{config.get("resolution")}.png'
        self.image_surface = pygame.image.load(self.image_path).convert_alpha()
        self.widgets = []
        self.widgets.append(Button(screen, (0, 0), 's' , 48, 40, 'start_button.png', 'start_button_hover.png', 'start_button_click.png'))
        self.widgets.append(Button(screen, (48, 0), 's', 344, 40, 'search_button.png', 'search_button_hover.png', 'search_button_click.png'))
        self.widgets.append(Button(screen, (392, 0), 's', 413, 40, 'blank_button.png', 'blank_button_hover.png', 'blank_button_click.png'))
        self.widgets.append(Button(screen, (0, 0), 'se', 5, 40, 'desktop_button.png', 'desktop_button_hover.png', 'desktop_button_click.png'))

    def render(self, mouse_pos, mouse_state):
        for widget in self.widgets:
            widget.render(mouse_pos, mouse_state)
