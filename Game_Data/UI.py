import pygame
import numpy as np

class Game_Object:
    def __init__(self, x, y, opacity = 1.0):
        self.x = x
        self.y = y
        self.opacity = opacity
    
    def update(self):
        pass

class Bubble_Object(Game_Object):
    def __init__(self, x, y, r, w = 0, color = (255,255,255), opacity=1):
        super().__init__(x, y, opacity)
        self.color = color
        self.r = r
        self.w = w
        self.velocity = np.array((0,-1))
        self.time = 0
        self.on_screen = True

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if (self.y+self.r<0):
            self.on_screen = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r, self.w)

class Animated_Background(Game_Object):
    def __init__(self, x, y, height, width, opacity = 1.0):
        super().__init__(x, y, height, width, opacity)

    def update(self):
        return

    def draw(self):
        return

class Text(Game_Object):
    def __init__(self, x, y, height, width, text = None, opacity = 1.0, font = 'Default'):
        super().__init__(self, x, y, opacity)
        self.height = height
        self.width = width
        self.text = text
        self.font = font
        return

    def update(self):
        return

class Button(Game_Object):
    def __init__(self, x, y, height, width, title = None, opacity = 1.0, state = 0):
        super().__init__(self, x, y, title, opacity)
        self.height = height
        self.width = width
        self.state = state
        self.icons = []
        self.sounds = []
        return

    def mouse_hover(self):
        return

    def mouse_on_click(self):
        return

    def mouse_on_release(self):
        return

    def update(self):
        return

class Main_Menu():
    def __init__(self):
        self.buttons = []
        self.bgms = []

        return

    def update(self):
        return