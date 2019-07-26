import math, random, pygame
import tkinter as tk
from tkinter import messagebox

# cube object
class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

# our snake object which will contain cube object
class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0
    y = 0

    for line in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w)) # vertical. x increases by 1 while y stays at 0
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y)) # horizontal. y increase by 1 while x stays at 0
    pass


def redraw_window(surface): # surface meaning the window plane
    global rows, w
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()



def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20 # the number of rows must divide evenly with the width
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))# the snake object. must pass color and position

    flag = True

    clock = pygame.time.Clock() # clock object
    while flag:
        pygame.time.delay(50) # speed option
        clock.tick(10) # makes sure the game does not run more than 10 fps
        redraw_window(win)

    pass


main()