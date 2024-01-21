import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)  # RGB value for white
YELLOW = (255, 255, 0)  # RGB value for yellow
BLUE = (100, 149, 237)  # RGB value for blue
RED = (178, 34, 34)  # RGB value for red
DARK_GREY = (105, 105, 105)  # RGB value for dark grey
BROWN = (139, 69, 19)  # RGB value for brown
LIGHT_BROWN = (222, 184, 135)  # RGB value for light brown
DARK_BLUE = (25, 25, 112)  # RGB value for dark blue
GREEN = (46, 139, 87)  # RGB value for green

FONT = pygame.font.SysFont("comicsans", 23)
