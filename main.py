import pygame

display_size = (600,400)
pygame.init()
screen = pygame.display.set_mode(display_size)
Clk = pygame.time.Clock()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
quit()