from planet import Planet
from constants import *


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30, "Sun", 0)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24, "Earth", 1)
    earth.y_velocity = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23, "Mars", 2)
    mars.y_velocity = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 0.330 * 10**24, "Mercury", 0)
    mercury.y_velocity = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24, "Venus", 0)
    venus.y_velocity = -35.02 * 1000

    jupiter = Planet(-5.203 * Planet.AU, 0, 25, BROWN, 1.8981 * 10 ** 27, "Jupiter", 0)
    jupiter.y_velocity = 13.06 * 1000

    saturn = Planet(9.537 * Planet.AU, 0, 25, LIGHT_BROWN, 5.6832 * 10 ** 26, "Saturn", 0)
    saturn.y_velocity = -9.67 * 1000

    neptune = Planet(30.068 * Planet.AU, 0, 20, DARK_BLUE, 1.204 * 10 ** 26, "Neptune", 0)
    neptune.y_velocity = -5.45 * 1000

    uranus = Planet(19.191 * Planet.AU, 0, 17, GREEN, 8.681 * 10 ** 25, "Uranus", 0)
    uranus.y_velocity = -6.79 * 1000

    planets = [sun, earth, mars, mercury, venus, jupiter, neptune, saturn, uranus]

    while run:
        clock.tick(60)
        WINDOW.fill((0, 0, 0))  # filling screen

        for event in pygame.event.get():  # list of all of the different events that occur
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WINDOW)
            planet.draw_moon(WINDOW)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
