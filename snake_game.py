import math, random, pygame
import tkinter as tk
from tkinter import messagebox

# cube object
class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):  # dirnx=1 means the snake starts moving right away
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color  # the 'snack' will be a different color than the snake

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):  # in pygame, you draw from the top left corner
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        # the 3rd parameter is to make the cube fill inside the grid lines. otherwise, the girds would disappear
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:  # draws the eyes
            centre = dis // 2
            radius = 3
            circle_middle = (i * dis + centre - radius, j * dis + 8)
            circle_middle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)

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

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
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


    def reset(self, pos):  # resets the snake so we can play again
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):  # find tail of body, then add to body if snack is eaten
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny

        # need to know which side of the snake to add the cube to
        # check what direction we are currently moving in to determine if we
        # need to add the cube to the left, right, above or below
        if dx == 1 and dy == 0:  # right
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:  # left
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:  # down
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:  # up
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        # set the cubes direction to the direction of the snake
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


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
    global rows, width, s, snack
    surface.fill((0, 0, 0))  # the surface color is black
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    #global rows
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:  # makes sure the snake does not appear on snake
            continue
        else:
            break

    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack  # you have to global each variable to be able to use it in other functions
    width = 500
    rows = 20  # the number of rows must divide evenly with the width
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))  # the snake object. must pass color and position
    snack = cube(random_snack(rows, s), color=(0,255,0))
    flag = True

    clock = pygame.time.Clock()  # clock object
    while flag:
        pygame.time.delay(50)  # speed option
        clock.tick(10)  # makes sure the game does not run more than 10 fps
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = cube(random_snack(rows, s), color=(0,255,0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda x:x.pos, s.body[x+1:])): # will check if any of the positions in our body list overlap
                print('score: ', len(s.body))
                message_box('You lost', 'Play again?')
                s.reset((10,10))
                break  # does not matter if we collide again

        redraw_window(win)


main()
