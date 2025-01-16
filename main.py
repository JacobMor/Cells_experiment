import pygame
import functiontools
from functiontools import Manager

display_size = (1200,600)
pygame.init()
screen = pygame.display.set_mode(display_size)
Clk = pygame.time.Clock()
man = Manager(display_size)
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    man.run()
    Clk.tick(120)

pygame.quit()
quit()