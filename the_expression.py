from re import X
import pygame
import argparse

x = 0
def setup():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    return screen, clock

def draw(screen, clock, FPS):
    global x
    x = (x + 1) % 256
    screen.fill((x,x,x))
    pygame.display.update()
    clock.tick(FPS)
    return 0


if __name__ == "__main__":
    
    exit = False
    FPS = 30

    screen, clock = setup()
    screen.fill((255,255,255))
    clock.tick(60)

    while (not(exit)):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit = True
        draw(screen, clock, FPS)

    pygame.quit()
    quit
