import math
from number_conversion import human_format
from constants import *
import pygame
pygame.init()


class Planet:
    AU = 149.6e6 * 1000  # astronomical units in meters
    G = 6.67428e-11  # gravitational constant
    SCALE = 25 / AU  # 1 AU = 100 pixels
    TIMESTEP = 3600*24  # 1 day

    def __init__(self, x, y, radius, color, mass, name, moon):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_velocity = 0
        self.y_velocity = 0

        self.moon = moon

        self.theta = 0
        self.phi = 0

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(window, self.color, False, updated_points, 2)

        pygame.draw.circle(window, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{self.name} {human_format(self.distance_to_sun/1000)}km", 1, WHITE)
            window.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_width()/2))

        if self.sun:
            name_text = FONT.render(f"{self.name}", 1, WHITE)
            window.blit(name_text, (x - name_text.get_width(), y + name_text.get_width()))

    def draw_moon(self, window):
        if self.moon == 1:
            x_center = self.x * self.SCALE + WIDTH / 2
            y_center = self.y * self.SCALE + HEIGHT / 2
            r = 0.15 * Planet.AU * self.SCALE

            x = r * math.cos(self.theta) + x_center
            y = r * math.sin(self.theta) + y_center
            self.theta -= math.pi / 40

            pygame.draw.circle(window, WHITE, (x, y), 4)

        elif self.moon == 2:  # mars
            # get center, and radius of the orbit
            x_center = self.x * self.SCALE + WIDTH / 2
            y_center = self.y * self.SCALE + HEIGHT / 2
            r1 = 0.15 * Planet.AU * self.SCALE  # deimos
            r2 = 0.10 * Planet.AU * self.SCALE

            # create the orbit of phobos
            x2 = r2 * math.cos(self.phi) + x_center
            y2 = r2 * math.sin(self.phi) + y_center
            self.phi -= math.pi / 30

            # create the orbit of deimos
            x1 = r1 * math.cos(self.theta) + x_center
            y1 = r1 * math.sin(self.theta) + y_center
            self.theta -= math.pi / 50

            pygame.draw.circle(window, BLUE, (x1, y1), 2)
            pygame.draw.circle(window, BROWN, (x2, y2), 3)

    def attraction(self, other):
        """
        Returns the force exerted upon this body by the other body.
        """
        # calculating distance between two objects
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        # calculating force of attraction
        force = self.G * self.mass * other.mass / distance**2
        # calculating angle
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        """
        Displays information about the status of the simulation.
        """
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_velocity += total_fx / self.mass * self.TIMESTEP
        self.y_velocity += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        self.orbit.append((self.x, self.y))
