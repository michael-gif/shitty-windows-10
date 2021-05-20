import pygame

from config import *

class Widget:
    def __init__(self, screen, pos, width, height):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height

class Button(Widget):
    def __init__(self, screen, pos, width, height, src, src_hover, src_click, command=None):
        super().__init__(screen, pos, width, height)
        self.offset = pos
        self.src = f'./resources/buttons/{src}'
        self.src_hover = f'./resources/buttons/{src_hover}'
        self.src_click = f'./resources/buttons/{src_click}'
        self.image = pygame.image.load(self.src).convert_alpha()
        self.image_hover = pygame.image.load(self.src_hover).convert_alpha()
        self.image_click = pygame.image.load(self.src_click).convert_alpha()
        self.command = command

        self.is_down = False

    def render(self, mouse_pos, mouse_state):
        if self.is_down:
            # check if the mouse is not being pressed
            if not mouse_state[0]:
                self.is_down = False
                if self.command != None:
                    self.command()
        # clicking the button
        if self.mouse_over(mouse_pos) and mouse_state[0]:
            self.screen.blit(self.image_click, self.pos)
            self.is_down = True
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
        res = [int(a) for a in config.get('resolution')['value'].split('x')]
        super().__init__(screen, (0, 0), res[0], res[1])
        self.image_path = f'./resources/background/{config.get("resolution")["value"]}.jpg'
        self.image_surface = None
        try:
            self.image_surface = pygame.image.load(self.image_path).convert_alpha()
        except:
            print(f'\nSyntaxError: unknown resolution provided: {config.get("resolution")["value"]}, failed to finding matching background')

    def render(self, mouse_pos, mouse_state):
        if self.image_surface != None:
            self.screen.blit(self.image_surface, self.pos)

class TaskBar(Widget):
    def __init__(self, screen):
        super().__init__(screen, (0, 0), 100, 100)
        config = Config()
        self.widgets = []
        x, y = screen.get_size()
        self.widgets.append(Button(screen, (0, y - 40), 48, 40, 'start_button.png', 'start_button_hover.png', 'start_button_click.png'))
        self.widgets.append(Button(screen, (48, y - 40), 344, 40, 'search_button.png', 'search_button_hover.png', 'search_button_click.png'))
        self.widgets.append(Button(screen, (x - 5, y - 40), 5, 40, 'desktop_button.png', 'desktop_button_hover.png', 'desktop_button_click.png'))
        self.widgets.append(Button(screen, (x - 53, y - 40), 48, 40, 'notifications_button.png', 'notifications_button_hover.png', 'notifications_button_click.png'))
        self.widgets.append(Button(screen, (x - 123, y - 40), 70, 40, 'calendar_button.png', 'calendar_button_hover.png', 'calendar_button_click.png'))
        self.widgets.append(Button(screen, (x - 159, y - 40), 36, 40, 'language_button.png', 'language_button_hover.png', 'language_button_click.png'))
        self.widgets.append(Button(screen, (x - 181, y - 40), 22, 40, 'sound_button.png', 'sound_button_hover.png', 'sound_button_click.png'))
        self.widgets.append(Button(screen, (x - 203, y - 40), 22, 40, 'network_button.png', 'network_button_hover.png', 'network_button_click.png'))
        self.widgets.append(Button(screen, (x - 227, y - 40), 24, 40, 'hidden_icons_button.png', 'hidden_icons_button_hover.png', 'hidden_icons_button_click.png'))

    def render(self, mouse_pos, mouse_state):
        x, y = self.screen.get_size()
        pygame.draw.rect(self.screen, (26, 39, 66), (392, y - 40, x - 619, 40), False)
        for widget in self.widgets:
            widget.render(mouse_pos, mouse_state)
