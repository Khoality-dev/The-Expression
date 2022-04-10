import os
from typing import Text
import cv2
import pygame
import numpy as np
from Game_Data.Core import Match

from Model.models import Face_Detector

face_icon = pygame.transform.scale(pygame.image.load('Game_Data/image/face_icon.png'), (32,32))
not_face_icon = pygame.transform.scale(pygame.image.load('Game_Data/image/not_face_icon.png'), (32,32))

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
    def __init__(self, x, y, text, size = 56, opacity = 100, font = 'freesansbold.ttf'):
        super().__init__(x, y, opacity)
        self.font = font
        self.font = pygame.font.Font(font, size)
        self.color = (0,0,0)
        self.text = text
        self.rendered = pygame.font.Font.render(self.font, self.text, True, self.color)
        self.height = self.rendered.get_height()
        self.width = self.rendered.get_width()
        self.size = size

    def set_text(self, text):
        self.text = text

    def update(self):
        self.rendered = pygame.font.Font.render(self.font, self.text, True, self.color)
        return

    def draw(self, screen):
        screen.blit(self.rendered, (self.x - (self.width/2), self.y- (self.height/2)))

class Button(Game_Object):
    def __init__(self, x, y, height, width, title = None, opacity = 1.0, state = 0):
        super().__init__(x, y, opacity)
        self.height = height
        self.width = width
        self.x -= self.width/2
        self.y -= self.height/2
        self.color = (255,255,255)
        self.text = Text_Object(self.x + width/2, self.y + height/2, text = title)
        self.state = state
        self.icons = []
        self.sounds = []
        return

    def mouse_normal(self):
        self.text.color = (0,0,0)
        self.color = (255,255,255)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return

    def mouse_hover(self):
        self.text.color = (255,255,255)
        self.color = (0,0,0)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        return

    def on_hover(self):
        return self.state==1

    def update(self):
        mouse_posx, mouse_posy = pygame.mouse.get_pos()
        last_state = self.state
        if (self.x <= mouse_posx and mouse_posx <= self.x + self.width and self.y <= mouse_posy and mouse_posy <= self.y + self.height):
            self.state = 1
        else:
            self.state = 0

        if self.state != last_state:
            if (self.state == 1):
                self.mouse_hover()
            elif self.state == 0:
                self.mouse_normal()
        self.text.update()
        return
    
    def draw(self, screen):
        #pygame.draw.rect(screen, self.color,(self.x, self.y, self.width, self.height))
        self.text.draw(screen)
        return

class Camera():
    def __init__(self, screen, pygame_camera, flip_x, flip_y, rotating_state):
        self.camera = pygame_camera
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.rotating_state = rotating_state

        first_cam, second_cam = self.get_output_transform()
        self.cam_size = (first_cam.get_width(), first_cam.get_height())
        screen_center = (screen.get_rect()[2]/2,screen.get_rect()[3]/2)
        self.portrait_1_loc = (screen_center[0]/2 - self.cam_size[0]/2,screen_center[1] - self.cam_size[1]/2)
        self.portrait_2_loc = ((screen_center[0] + screen_center[0]/2) - self.cam_size[0]/2,screen_center[1] - self.cam_size[1]/2)


    def rotate(self):
        self.rotating_state = (self.rotating_state + 1) % 4
        return

    def flip_on_x(self):
        self.flip_x = not self.flip_x
        return
    
    def flip_on_y(self):
        self.flip_y = not self.flip_y
        return

    def get_output_transform(self):
        cam_image = pygame.transform.rotate(self.camera.get_image(), angle = (self.rotating_state)*90)
        cam_image = pygame.transform.flip(cam_image, flip_x = self.flip_x, flip_y = self.flip_y)
        (cam_width, cam_height) = cam_image.get_rect()[2], cam_image.get_rect()[3]
        first_cam = pygame.transform.chop(cam_image, (cam_width/2, 0, cam_width/2,0))
        second_cam = pygame.transform.chop(cam_image, (0, 0, cam_width/2,0))
        return first_cam, second_cam

    def draw(self, screen):
        first_cam, second_cam = self.get_output_transform()
        screen.blit(first_cam, self.portrait_1_loc)
        screen.blit(second_cam, self.portrait_2_loc)

        
            

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

    def draw(self, screen):
        self.screen.fill((210,210,210))
        for bubble_idx in range(len(self.bubble_list)):
            if self.bubble_list[bubble_idx].on_screen == False:
                img_path = os.path.join("Game_Data/emojis", np.random.choice(self.emojis_files))
                self.bubble_list[bubble_idx].reset(img_path, x = np.random.randint(0,self.screen.get_rect()[2]), y = np.random.randint(self.screen.get_rect()[3],self.screen.get_rect()[3] + 100))
            self.bubble_list[bubble_idx].update()
            self.bubble_list[bubble_idx].draw(screen = self.screen)
        return

class Main_Menu():
    def __init__(self, screen):
        self.screen = screen
        center_x, center_y = screen.get_rect()[2]/2, screen.get_rect()[3]/2
        self.buttons = [Button(x = center_x, y = center_y + 100, height = 60, width = 120, title = "Play"),
                        Button(x = center_x, y = center_y + 200, height = 60, width = 120, title = "Camera Setting"),
                        Button(x = center_x, y = center_y + 300, height = 60, width = 120, title = "Exit")]
        self.bgms = []
        self.logo = pygame.image.load("Game_Data/image/The Expression-logo.png")
        self.logo = pygame.transform.scale(self.logo, (screen.get_rect()[2]/3.85,screen.get_rect()[3]/2.5))
        return
    
    def update(self):
        for button in self.buttons:
            button.update()
        return

    def draw(self, screen):
        self.screen.blit(self.logo, ((self.screen.get_rect()[2]/2)-(self.logo.get_rect()[2]/2),self.screen.get_rect()[3]/2.5 - (self.logo.get_rect()[3]/2)))
        for button in self.buttons:
            button.draw(screen)
        return


class Camera_Menu():
    def __init__(self, camera, screen, FDetector):
        self.screen = screen
        self.camera = camera
        self.FDetector = FDetector
        center_x, center_y = screen.get_rect()[2]/2, screen.get_rect()[3]/2
        self.buttons = [Button(x = center_x, y = center_y - 200, height = 60, width = 120, title = "Rotate"),
                        Button(x = center_x, y = center_y - 100, height = 60, width = 120, title = "Flip x axis"),
                        Button(x = center_x, y = center_y, height = 60, width = 120, title = "Flip y axis"),
                        Button(x = center_x, y = center_y + 200, height = 60, width = 120, title = "<< Back")]
        self.bgms = []
        return
    
    
    def update(self):
        for button in self.buttons:
            button.update()


    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

        cam1, cam2 = self.camera.get_output_transform()

        img_cam1 = cv2.rotate(cv2.cvtColor(pygame.surfarray.array3d(cam1), cv2.COLOR_RGB2GRAY), cv2.ROTATE_90_CLOCKWISE)
        isFace = self.FDetector.predict(np.array(img_cam1))
        if (len(isFace) != 0):
            screen.blit(face_icon, (self.camera.portrait_1_loc[0], self.camera.portrait_1_loc[1] - face_icon.get_size()[1]))
        else:
            screen.blit(not_face_icon, (self.camera.portrait_1_loc[0], self.camera.portrait_1_loc[1] - not_face_icon.get_size()[1]))

        img_cam2 = cv2.rotate(cv2.cvtColor(pygame.surfarray.array3d(cam2), cv2.COLOR_RGB2GRAY), cv2.ROTATE_90_CLOCKWISE)
        isFace = self.FDetector.predict(np.array(img_cam2))
        if (len(isFace) != 0):
            screen.blit(face_icon, (self.camera.portrait_2_loc[0], self.camera.portrait_2_loc[1] - face_icon.get_size()[1]))
        else:
            screen.blit(not_face_icon, (self.camera.portrait_2_loc[0], self.camera.portrait_2_loc[1] - not_face_icon.get_size()[1]))

        self.camera.draw(screen)
        return

class Play_Menu():
    def __init__(self, AVEstimator, FDetector, FLDetector, camera, screen):
        self.screen = screen
        self.camera = camera
        
        center_x, center_y = screen.get_rect()[2]/2, screen.get_rect()[3]/2

        self.AVEstimator = AVEstimator
        self.FDetector = FDetector
        self.FLDetector= FLDetector
        self.round = Match(self.camera, self.FDetector, self.FLDetector, self.AVEstimator, length_in_milisec = 30*1000)
        self.starting = pygame.time.get_ticks()
        self.timer_display = Text_Object(center_x, 50, str(round(self.round.get_countdown()/1000,2)))

        self.target_image_surf = pygame.transform.rotate(pygame.surfarray.make_surface(self.round.target), -90)
        self.buttons = [Button(center_x/2 , center_y*2 - center_y/5, 60,120,"Replay"),
                        Button(center_x*2 - center_x/2, center_y*2 - center_y/5, 60, 120, "Return to Menu")]

        self.bgms = []
        self.text_score_p1 = Text_Object(center_x - (screen.get_rect()[2] / 4),center_y / 5, "Score: "+str(self.round.player_1_score))
        self.text_score_p2 = Text_Object(center_x + (screen.get_rect()[2] / 4),center_y / 5, "Score: "+str(self.round.player_2_score))

    def update(self):
        if not(self.round.isEnd()):
            self.round.update()
            if (self.round.state == 0):
                countdown = max(5000 - (pygame.time.get_ticks() - self.starting), 0)
                if (countdown <= 0):
                    self.round.start()
                    return
                else:
                    self.timer_display.set_text(str(round((5000 - (pygame.time.get_ticks() - self.starting))/1000)))
                    self.timer_display.update()

            if (self.round.state == 1):
                self.timer_display.set_text(str(round(self.round.get_countdown()/1000,2)))
                self.timer_display.update()
                self.text_score.set_text(str(self.round.player_1_score))
                self.text_score.update()
        else:
            for button in self.buttons:
                button.update()

        return

    def draw(self, screen):
        
        if not(self.round.isEnd()):
            self.timer_display.draw(screen)
            self.screen.blit(self.target_image_surf, (self.screen.get_rect()[2]/2 - self.target_image_surf.get_size()[0]/2, self.screen.get_rect()[3]/2 - self.target_image_surf.get_size()[1]/2))
            self.camera.draw(screen)
            self.text_score.draw(screen)

            if (self.round.player_1_score == 0):
                self.screen.blit(not_face_icon, (self.camera.portrait_1_loc[0], self.camera.portrait_1_loc[1] - face_icon.get_size()[1]))
            else:
                self.screen.blit(face_icon, (self.camera.portrait_1_loc[0], self.camera.portrait_1_loc[1] - not_face_icon.get_size()[1]))

            if (self.round.player_2_score == 0):
                self.screen.blit(not_face_icon, (self.camera.portrait_2_loc[0], self.camera.portrait_2_loc[1] - face_icon.get_size()[1]))
            else:
                self.screen.blit(face_icon, (self.camera.portrait_2_loc[0], self.camera.portrait_2_loc[1] - not_face_icon.get_size()[1]))
            
        else:
            if type(self.round.player_1_best_face) is pygame.Surface:
                img_pos_x, img_pos_y = self.camera.portrait_1_loc[0]+50, self.camera.portrait_1_loc[1]
                score = Text_Object(img_pos_x + self.camera.cam_size[0]/2, 0, str(self.round.player_1_best_score))
                score.y = img_pos_y - score.height
                score.update()
                score.draw(screen)
                screen.blit(self.round.player_1_best_face, (img_pos_x, img_pos_y))
            if type(self.round.player_2_best_face) is pygame.Surface:
                img_pos_x, img_pos_y = self.camera.portrait_2_loc[0]-50, self.camera.portrait_2_loc[1]
                score = Text_Object(img_pos_x + self.camera.cam_size[0]/2, 0, str(self.round.player_2_best_score))
                score.y = img_pos_y - score.height
                score.update()
                score.draw(screen)
                screen.blit(self.round.player_2_best_face, (self.camera.portrait_2_loc[0]-50, self.camera.portrait_2_loc[1]))

            for button in self.buttons:
                button.draw(self.screen)
        return