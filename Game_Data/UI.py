import os
from re import S
import pygame
import numpy as np

class Game_Object:
    def __init__(self, x, y, opacity = 100):
        self.x = x
        self.y = y
        self.opacity = opacity
    
    def update(self):
        pass

class Bubble_Object(Game_Object):
    def __init__(self, img_path, x, y, size, opacity=1):
        super().__init__(x, y, opacity)
        self.ico = pygame.image.load(img_path)
        self.size = (size,size)
        self.velocity = np.array((0,-1))
        self.time = 0
        self.on_screen = True

    def reset(self, img_path, x, y):
        self.ico = self.ico = pygame.image.load(img_path)
        self.x, self.y = x, y
        self.on_screen = True
        
        return
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if (self.y<-10):
            self.on_screen = False

    def draw(self, screen):
        screen.blit(self.ico, (self.x, self.y))


class Text_Object(Game_Object):
    def __init__(self, x, y, size, text, opacity = 100, font = 'Default'):
        super().__init__(x, y, opacity)
        self.font = font
        self.font = pygame.font.Font(font, size)
        self.text = pygame.font.Font.render(self.font, text, True, (0,0,0))
        self.size = size
    def update(self):
        return

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))

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

class Animated_Background(Game_Object):
    def __init__(self, screen):
        self.screen = screen
        self.bubble_list = []
        self.emojis_files = [f for f in os.listdir("Game_Data/emojis") if os.path.isfile(os.path.join("Game_Data/emojis", f)) and (os.path.splitext(f)[1] == '.png')]
        for i in range(20):
            size = np.random.randint(5,20)
            img_path = os.path.join("Game_Data/emojis", np.random.choice(self.emojis_files))
            bubble = Bubble_Object(img_path, x = np.random.randint(0,self.screen.get_rect()[2]), y = np.random.randint(0,self.screen.get_rect()[3]), size = size)
            self.bubble_list.append(bubble)

    def draw(self):
        for bubble_idx in range(len(self.bubble_list)):
            if self.bubble_list[bubble_idx].on_screen == False:
                img_path = os.path.join("Game_Data/emojis", np.random.choice(self.emojis_files))
                self.bubble_list[bubble_idx].reset(img_path, x = np.random.randint(0,self.screen.get_rect()[2]), y = np.random.randint(self.screen.get_rect()[3],self.screen.get_rect()[3] + 100))
            self.bubble_list[bubble_idx].update()
            self.bubble_list[bubble_idx].draw(screen = self.screen)
        return

class Main_Menu():
    def __init__(self):
        self.buttons = []
        self.bgms = []

        
        return

    def draw(self):
        
        return