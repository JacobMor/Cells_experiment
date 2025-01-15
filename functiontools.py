import pygame
from random import randint


class Microbe:
    """Main cells class. Has energy, ID to interact with other Microbes, current coordinates, and coordinates to move to
    Has boolean parameter of reaching end point
    """

    def __init__(self, display_size: tuple):
        """

        :type display_size: Ranges move coordinates
        """
        self.screen = pygame.display.set_mode(display_size)
        self.energy = 600
        self.coordinates_x = 250
        self.coordinates_y = 250
        self.dest_coordinates_x = 0
        self.dest_coordinates_y = 0
        self.end_point_reached = False
        self.image = pygame.image.load()  # TODO image lo load

    def draw(self):
        self.screen.blit(self.image, (self.coordinates_x, self.coordinates_y))


class Food(Microbe):
    """Has energy to feed Microbes. """

    def __init__(self, display_size: tuple):
        super().__init__(display_size)
        self.energy = 600
        self.coordinates_x = randint(10, display_size[0] -10)
        self.coordinates_y = randint(10, display_size[1] -10)



class Manager:
    """Manages display, giving new coordinates. Counts new stats of elements. Contains list of elements."""

    def __init__(self, display_size: tuple):
        self.screen = pygame.display.set_mode(display_size)
        self.microbes_list = [Microbe(display_size)]
        self.food_list = [Food(display_size)]
        self.action_list = []  # list that accepts objects for interaction

    def run(self):  # main function contains manager logic
        pass

    def new_coordinates(self):
        return

    def draw(self):
        for microbe in self.microbes_list:
            microbe.draw()

        for food in self.food_list:
            food.draw()


