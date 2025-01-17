import pygame
from pygame import mouse
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            man.add_food(position=pygame.mouse.get_pos())

    man.run()
    Clk.tick(30)

pygame.quit()
quit()