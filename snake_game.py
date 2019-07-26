import math, random, pygame
import tkinter as tk
from tkinter import messagebox

# cube object
class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):  # dirnx=1 means the snake starts moving right away
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color  # the 'snack' will be a different color than the snake

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        pass

# our snake object which will contain cube object
class snake(object):
    body = [] # list
    turns = {} # class variable. this remembers where the head turned so the body can follow

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # the head is the cube object at a given position
        self.body.append(self.head)  # add to head
        # snake can only move in one direction at a time. -1, 0, 1 will indicate up, down, left, right, or not moving
        self.dirnx = 0  # up or down
        self.dirny = 1  # left or right. if one is 0, the other must be 1 or -1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()  # key object. acts like a dictionary

            # for any key pressed, you can dictate what action to take
            # pygame coordinates start at 0,0 at the top most left
            for key in keys:
                if keys[pygame.K_LEFT]:  # x: -1 means closer to 0
                    self.dirnx = -1
                    self.dirny = 0  # must be 0 as we dont want to move in 2 direction at at time
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # the body follows head
                        # self.head.pos is the 'key' and it is set (value) to what direction the head turned
                elif keys[pygame.K_RIGHT]: # x: 1 means away from 0
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif key[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif key[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):  # we are enumerating the index and cube object
            p = c.pos[:]  # for each object (c), we grab their pos and see if in turn list
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)

            else:  # code for body to continue to move
                if c.dirnx == -1 and c.pos[0] <= 0:  # checking if we reached the edge of screen
                    c.pos = (c.rows - 1, c.pos[1])  # move across screen
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:  # if moving right, then go to left side cf screen
                    c.pos = (0, c.pos[1])  # 0 indicates left side of screen
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)  # move to top of screen
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows -1)  # move to bottom of screen
                else:
                    c.move(c.dirnx, c.dirny)  # if not at edge of screen, then simply we just move




    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # this checks and tracks the first cube
                c.draw(surface, True)  # the True creates eyes on the first cube
            else:
                c.draw(surface)  # draws the rest of the body


def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0
    y = 0

    for line in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))  # vertical. x increases by 1 while y stays at 0
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # horizontal. y increase by 1 while x stays at 0


def redraw_window(surface):  # surface meaning the window plane
    global rows, width, s
    surface.fill((0, 0, 0))  # the surface color is black
    s.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()



def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 400
    rows = 20  # the number of rows must divide evenly with the width
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))  # the snake object. must pass color and position

    flag = True

    clock = pygame.time.Clock()  # clock object
    while flag:
        pygame.time.delay(50)  # speed option
        clock.tick(10)  # makes sure the game does not run more than 10 fps
        redraw_window(win)

    pass


main()