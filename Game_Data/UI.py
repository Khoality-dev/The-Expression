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
    def __init__(self, x, y, r, w = 0, color = (255,255,255), velocity = np.zeros(2, dtype=np.int32), lifetime = np.random.randint(10,1000), opacity=np.random.randint(100,500)):
        super().__init__(x, y, opacity)
        self.color = color
        self.r = r
        self.w = w
        self.velocity = velocity
        self.acceleration = np.zeros(2, dtype=np.int32)

        self.lifetime = lifetime
        self.surface = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, self.color, (self.r,self.r), self.r, self.w)

    def decrease_velocity(self):
        self.acceleration[0] = -np.sign(self.velocity[0])
        self.acceleration[1] = -np.sign(self.velocity[1])

        if np.abs(self.velocity).any() > 0:
            self.velocity += self.acceleration
        else:
            self.velocity = np.zeros(2, dtype=np.int32)

    def update(self):
        if self.lifetime > 0:
            self.lifetime += -1
        else:
            if (self.opacity > 0):
                self.opacity += -2

        self.x += self.velocity[0]
        self.y += self.velocity[1]


    def draw(self, screen):
        self.surface.set_alpha(self.opacity)
        screen.blit(self.surface, (self.x, self.y))

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