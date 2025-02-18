import pygame
from random import randint
import logic


class Microbe:
    """Main cells class. Has energy, ID to interact with other Microbes, current coordinates, and coordinates to move to
    Has boolean parameter of reaching end point
    """

    def __init__(self, display_size: tuple, coordinates: tuple = (250, 250)):
        """

        :type coordinates: start coordinates
        :type display_size: Ranges move coordinates
        """
        self.screen = pygame.display.set_mode(display_size)
        self.screen_borders = display_size
        self.energy = 600
        self.coordinates_x = coordinates[0]
        self.coordinates_y = coordinates[1]
        self.dest_coordinates_x = 250
        self.dest_coordinates_y = 250
        self.image = pygame.image.load("D:\\shada\\Documents\\Cells_experiment\\Microbe.png")
        self.fontObj = pygame.font.Font(None, 18) # for text above microbe and food

    def draw(self):
        self.screen.blit(self.image, (self.coordinates_x, self.coordinates_y))
        # energy above each microbe
        text_surface_obj = self.fontObj.render(str(self.energy), True, (255, 255, 255), None)
        self.screen.blit(text_surface_obj, (self.coordinates_x, self.coordinates_y - 10))  # energy display

    def reached_destination(self):
        if self.coordinates_x == self.dest_coordinates_x and self.coordinates_y == self.dest_coordinates_y:
            return True
        else:
            return False

    def new_random_destination(self):
        """function choosing new random coordinates, x,y"""
        self.dest_coordinates_x = randint(10, self.screen_borders[0] - 10)  # new according to screen borders
        self.dest_coordinates_y = randint(10, self.screen_borders[1] - 10)
        self.draw()

    def energy_consumption(self, energy: int):
        """decreases amount of energy"""
        self.energy -= energy

    def energy_replenishment(self, energy: int):
        """increases amount of energy"""
        self.energy += energy


class Food(Microbe):
    """Has energy to feed Microbes. """

    def __init__(self, display_size: tuple, coordinates: tuple):
        super().__init__(display_size)
        self.energy = 2000
        self.image = pygame.image.load("D:\\shada\\Documents\\Cells_experiment\\Food.png")
        self.coordinates_x = coordinates[0]
        self.coordinates_y = coordinates[1]


class Manager:
    """Manages display, giving new coordinates. Counts new stats of elements. Contains list of elements."""

    def __init__(self, display_size: tuple):
        self.screen = pygame.display.set_mode(display_size)
        self.microbes_list = [Microbe(display_size)]
        self.food_list = []
        self.distance = pygame.math.Vector2
        self.field = display_size

    def run(self):  # main function contains manager logic
        self.screen.fill((0, 0, 0))
        self.distance_check(self.microbes_list, self.food_list)  # check distance to food
        for microbe in self.microbes_list:  # checking if someone reached destination, and moving
            if microbe.reached_destination():
                microbe.new_random_destination()
            else:
                self.move(microbe)
            microbe.energy_consumption(1)
        self.object_kill(self.microbes_list)  # delete microbe without energy
        if self.food_list:  # actions with food
            self.object_kill(self.food_list)  # delete eaten food
            if self.food_list:
                for food in self.food_list:
                    food.draw()
            else:
                pass
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

    def distance_check(self, microbes: list, food: list):
        """check distances between objects in list of objects, adds energy, takes energy, activates cell add"""
        if microbes:
            if food:
                for microbe in microbes:
                    for f in food:
                        if int(self.distance(microbe.coordinates_x, microbe.coordinates_y).distance_to(
                                (f.coordinates_x, f.coordinates_y))) <= 150:
                            microbe.dest_coordinates_x = f.coordinates_x
                            microbe.dest_coordinates_y = f.coordinates_y
                        if int(self.distance(microbe.coordinates_x, microbe.coordinates_y).distance_to(
                                (f.coordinates_x, f.coordinates_y))) <= 20:  # feeding in area of food
                            microbe.energy_replenishment(20)
                            f.energy_consumption(20)
                            if microbe.energy >= 1000:
                                self.add_cell(position=(microbe.coordinates_x, microbe.coordinates_y))
                                microbe.energy -= 600
                        else:
                            pass

    def add_food(self, position: tuple):
        self.food_list.append(Food(self.field, position))

    def add_cell(self, position: tuple):
        self.microbes_list.append(Microbe(self.field, position))

    def object_kill(self, list_of_objects: list):
        """delete objects if energy is zero"""
        for element in list_of_objects:
            if element.energy <= 0:
                list_of_objects.remove(element)
            else:
                pass
