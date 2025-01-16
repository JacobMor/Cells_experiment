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
        self.screen_borders = display_size
        self.energy = 600
        self.coordinates_x = 250
        self.coordinates_y = 250
        self.dest_coordinates_x = 50
        self.dest_coordinates_y = 50
        self.image = pygame.image.load("D:\\shada\\Documents\\Cells_experiment\\Microbe.png")

    def draw(self):
        self.screen.blit(self.image, (self.coordinates_x, self.coordinates_y))

    def reached_destination(self):
        if self.coordinates_x == self.dest_coordinates_x and self.coordinates_y == self.dest_coordinates_y:
            return True
        else:
            return False

    def new_random_destination(self):
        """function choosing new random coordinates, x,y"""
        self.dest_coordinates_x = randint(10, self.screen_borders[0] - 10)  # new coord -10 by x
        self.dest_coordinates_y = randint(10, self.screen_borders[1] - 10)  # new coord -10 by y


class Food(Microbe):
    """Has energy to feed Microbes. """

    def __init__(self, display_size: tuple):
        super().__init__(display_size)
        self.energy = 600
        self.image = pygame.image.load("D:\\shada\\Documents\\Cells_experiment\\Food.png")
        self.coordinates_x = randint(10, display_size[0] - 10)
        self.coordinates_y = randint(10, display_size[1] - 10)


class Manager:
    """Manages display, giving new coordinates. Counts new stats of elements. Contains list of elements."""

    def __init__(self, display_size: tuple):
        self.screen = pygame.display.set_mode(display_size)
        self.microbes_list = [Microbe(display_size), Microbe(display_size), Microbe(display_size),
                              Microbe(display_size), Microbe(display_size), Microbe(display_size),
                              Microbe(display_size)]
        self.food_list = [Food(display_size)]
        self.action_list = []  # list that accepts objects for interaction(changing destination)

    def run(self):  # main function contains manager logic
        self.screen.fill((0, 0, 0))
        for microbe in self.microbes_list:  # checking if someone reached destination
            if microbe.reached_destination():
                microbe.new_random_destination()
            else:
                self.move(microbe)
        pygame.display.update()

    def move(self, microbe):
        if microbe.coordinates_x < microbe.dest_coordinates_x:
            microbe.coordinates_x += 1
        elif microbe.coordinates_x > microbe.dest_coordinates_x:
            microbe.coordinates_x -= 1
        else:
            pass
        if microbe.coordinates_y < microbe.dest_coordinates_y:
            microbe.coordinates_y += 1
        elif microbe.coordinates_y > microbe.dest_coordinates_y:
            microbe.coordinates_y -= 1
        else:
            pass
        microbe.draw()

    def distance_check(self):
        """check distances between objects in list of objects"""
        pass
