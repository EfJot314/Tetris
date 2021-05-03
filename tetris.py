import pygame
import sys
import random


from pygame.locals import *

pygame.init()
bok = 20
plansza = pygame.display.set_mode((12*bok, 22*bok))
pygame.display.set_caption('Tetris')

czcionka = pygame.font.SysFont("monospace",30)

zegar = pygame.time.Clock()
FPS = 100


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (105, 105, 105)
GREEN = (124, 252, 0)
BLUE = (135, 206, 250)
DEEP_BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
PURPLE = (139, 0, 139)
RED = (255, 0, 0)


class tetr:
    def __init__(self, x, y, rot):
        self.x = x
        self.y = y
        self.rot = rot
        self.mov = True
        

class I(tetr):
    def change(self, var):
        if self.mov:
            self.rot += 1
            if self.rot == 4:
                self.rot = 0
            if self.rot == 0 or self.rot == 2: 
                if pl[self.x-1][self.y] == 1:
                    self.x += 2
                    if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                        self.x -= 2
                        self.rot = 1
                elif pl[self.x-2][self.y] == 1:
                    self.x += 1
                    if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                        self.x -= 1
                        self.rot = 1
                elif pl[self.x+1][self.y] == 1:
                    self.x -= 1
                    if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                        self.x += 1
                        self.rot = 1
                if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                        self.rot = 1
            else:
                if pl[self.x][self.y-3] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    self.rot = 0
                    
    
    def move(self, var):
        if var == 'l':
            if self.rot == 0 or self.rot == 2:
                if pl[self.x-3][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            else:
                if pl[self.x-1][self.y-3] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
        else:
            if self.rot == 0 or self.rot == 2:
                if pl[self.x+2][self.y] == 1:
                    pass
                else:
                    self.x += 1
            else:
                if pl[self.x+1][self.y-3] == 1 or pl[self.x+1][self.y-2] == 1 or pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            if self.rot == 0 or self.rot == 2:
                pl[self.x-2][self.y] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
            else:
                pl[self.x][self.y-3] = 1
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
        if self.rot == 0 or self.rot == 2:
            if pl[self.x-2][self.y+1] == 1 or pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1 or pl[self.x+1][self.y+1] == 1:
                self.mov = False
                pl[self.x-2][self.y] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
        else:
            if pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x][self.y-3] = 1
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1

    def colors(self, clt):
        if self.rot == 0 or self.rot == 2:
            clt[self.x-2][self.y] = BLUE
            clt[self.x-1][self.y] = BLUE
            clt[self.x][self.y] = BLUE
            clt[self.x+1][self.y] = BLUE
        else:
            clt[self.x][self.y-3] = BLUE
            clt[self.x][self.y-2] = BLUE
            clt[self.x][self.y-1] = BLUE
            clt[self.x][self.y] = BLUE

    def show(self, plansza):
        if self.rot == 0 or self.rot == 2:
            pygame.draw.rect(plansza, BLUE, ((self.x-2)*bok, self.y*bok, 4*bok, bok))
        else:
            pygame.draw.rect(plansza, BLUE, (self.x*bok, (self.y-3)*bok, bok, 4*bok))

class O(tetr):
    def change(self, var):
        pass

    def move(self, var):
        if var == 'l':
            if pl[self.x-2][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                pass
            else:
                self.x -= 1
        else:
            if pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                pass
            else:
                self.x += 1
    

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            pl[self.x-1][self.y-1] = 1
            pl[self.x][self.y-1] = 1
            pl[self.x-1][self.y] = 1
            pl[self.x][self.y] = 1
        if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1:
            self.mov = False
            pl[self.x-1][self.y-1] = 1
            pl[self.x][self.y-1] = 1
            pl[self.x-1][self.y] = 1
            pl[self.x][self.y] = 1


    def colors(self, clt):
        clt[self.x-1][self.y-1] = YELLOW
        clt[self.x][self.y-1] = YELLOW
        clt[self.x-1][self.y] = YELLOW
        clt[self.x][self.y] = YELLOW

    def show(self, plansza):
        pygame.draw.rect(plansza, YELLOW, ((self.x-1)*bok, (self.y-1)*bok, 2*bok, 2*bok))
    
class L(tetr):
    def change(self, var):
        if self.mov:
            if var == 0:
                self.rot += 1
                if self.rot == 4:
                    self.rot = 0
                if self.rot == 0: 
                    if pl[self.x][self.y] == 1 or pl[self.x-1][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.x += 1
                            self.rot = 3

                    if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.rot = 3

                elif self.rot == 1:
                    if pl[self.x][self.y-1] == 1:
                        self.x -= 1
                        if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x += 1
                            self.rot = 0
                    elif pl[self.x-2][self.y] == 1:
                        self.x += 1
                        if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x -= 1
                            self.rot = 0

                    if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x][self.y-1] == 1:
                        self.rot = 0
                elif self.rot == 2:
                    if pl[self.x][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x += 1
                            self.rot = 1
                    elif pl[self.x-1][self.y-2] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x -= 1
                            self.rot = 1

                    if pl[self.x-1][self.y-2] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.rot = 1
                elif self.rot == 3:
                    if pl[self.x+1][self.y-1] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y-1] == 1:
                            self.x += 1
                            self.rot = 2
                    elif pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y-1] == 1:
                            self.x -= 1
                            self.rot = 2

                    if pl[self.x-1][self.y] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y-1] == 1:
                            self.rot = 2

            else:
                self.rot -= 1
                if self.rot == -1:
                    self.rot = 3
                if self.rot == 0: 
                    if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y-2] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.x -= 1
                            self.rot = 1

                    if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                        self.rot = 1

                elif self.rot == 1:
                    if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1:
                        self.x += 1
                        if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x -= 1
                            self.rot = 2

                    if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.rot = 2
                        
                    
                elif self.rot == 2:
                    if pl[self.x][self.y] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x += 1
                            self.rot = 3

                    elif pl[self.x][self.y-2] == 1 or pl[self.x-1][self.y-2] == 1:
                        self.rot = 3

                elif self.rot == 3:
                    if pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y-1] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y-1] == 1:
                            self.x += 1
                            self.rot = 0

                    if pl[self.x-1][self.y] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y-1] == 1:
                            self.rot = 0
                    


    def move(self, var):
        if var == 'l':
            if self.rot == 0:
                if pl[self.x-2][self.y-2] == 1 or pl[self.x-2][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 1:
                if pl[self.x-3][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 2:
                if pl[self.x-2][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 3:
                if pl[self.x-2][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                    pass
                else:
                    self.x -= 1
        else:
            if self.rot == 0:
                if pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 1:
                if pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 2:
                if pl[self.x+1][self.y-2] == 1 or pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 3:
                if pl[self.x+2][self.y-1] == 1 or pl[self.x][self.y] == 1:
                    pass
                else:
                    self.x += 1

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            if self.rot == 0:
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
            elif self.rot == 1:
                pl[self.x-2][self.y] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x][self.y-1] = 1
            elif self.rot == 2:
                pl[self.x-1][self.y-2] = 1
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
            elif self.rot == 3:
                pl[self.x-1][self.y] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x+1][self.y-1] = 1
            
        if self.rot == 0:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
        elif self.rot == 1:
            if pl[self.x-2][self.y+1] == 1 or pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x-2][self.y] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x][self.y-1] = 1
        elif self.rot == 2:
            if pl[self.x][self.y+1] == 1 or pl[self.x-1][self.y-1] == 1:
                self.mov = False
                pl[self.x-1][self.y-2] = 1
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
        elif self.rot == 3:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                self.mov = False
                pl[self.x-1][self.y] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x+1][self.y-1] = 1

    def colors(self, clt):
        if self.rot == 0:
            clt[self.x-1][self.y-2] = ORANGE
            clt[self.x-1][self.y-1] = ORANGE
            clt[self.x-1][self.y] = ORANGE
            clt[self.x][self.y] = ORANGE
        elif self.rot == 1:
            clt[self.x-2][self.y] = ORANGE
            clt[self.x-1][self.y] = ORANGE
            clt[self.x][self.y] = ORANGE
            clt[self.x][self.y-1] = ORANGE
        elif self.rot == 2:
            clt[self.x-1][self.y-2] = ORANGE
            clt[self.x][self.y-2] = ORANGE
            clt[self.x][self.y-1] = ORANGE
            clt[self.x][self.y] = ORANGE
        elif self.rot == 3:
            clt[self.x-1][self.y] = ORANGE
            clt[self.x-1][self.y-1] = ORANGE
            clt[self.x][self.y-1] = ORANGE
            clt[self.x+1][self.y-1] = ORANGE

    def show(self, plansza):
        if self.rot == 0:
            pygame.draw.rect(plansza, ORANGE, ((self.x-1)*bok, (self.y-2)*bok, bok, 3*bok))
            pygame.draw.rect(plansza, ORANGE, (self.x*bok, self.y*bok, bok, bok))
        elif self.rot == 1:
            pygame.draw.rect(plansza, ORANGE, (self.x*bok, (self.y-1)*bok, bok, 2*bok))
            pygame.draw.rect(plansza, ORANGE, ((self.x-2)*bok, self.y*bok, 2*bok, bok))
        elif self.rot == 2:
            pygame.draw.rect(plansza, ORANGE, (self.x*bok, (self.y-1)*bok, bok, 2*bok))
            pygame.draw.rect(plansza, ORANGE, ((self.x-1)*bok, (self.y-2)*bok, 2*bok, bok))
        elif self.rot == 3:
            pygame.draw.rect(plansza, ORANGE, ((self.x-1)*bok, (self.y-1)*bok, bok, 2*bok))
            pygame.draw.rect(plansza, ORANGE, (self.x*bok, (self.y-1)*bok, 2*bok, bok))

class J(tetr): 
    def change(self, var):
        if self.mov:
            if var == 0:
                self.rot += 1
                if self.rot == 4:
                    self.rot = 0
                if self.rot == 0: 
                    if pl[self.x][self.y-1] == 1 or pl[self.x][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y] == 1:
                            self.x += 1
                            self.rot = 3

                    if pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y] == 1:
                            self.rot = 3

                elif self.rot == 1:
                    if pl[self.x-2][self.y-1] == 1:
                        self.x -= 1
                        if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x += 1
                            self.rot = 0

                    if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.rot = 0
                    
                elif self.rot == 2:
                    if pl[self.x-1][self.y] == 1:
                        self.x += 1
                        if pl[self.x][self.y-2] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.x -= 1
                            self.rot = 1
                    elif pl[self.x][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x][self.y-2] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.x += 1
                            self.rot = 1

                    if pl[self.x][self.y-2] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.rot = 1

                elif self.rot == 3:
                    if pl[self.x][self.y] == 1:
                        self.x -= 2
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                            self.x += 2
                            self.rot = 2
                    elif pl[self.x+1][self.y] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                            self.x += 1
                            self.rot = 2

                    if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                            self.rot = 2

            else:
                self.rot -= 1
                if self.rot == -1:
                    self.rot = 3
                if self.rot == 0: 
                    if pl[self.x-1][self.y] == 1:
                        self.x += 1
                        if pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y] == 1:
                            self.x -= 1
                            self.rot = 1

                    if pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y] == 1:
                            self.rot = 1

                elif self.rot == 1:
                    if pl[self.x-2][self.y-1] == 1:
                        self.x += 1
                        if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x -= 1
                            self.rot = 2
                    elif pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                        self.x -= 1
                        if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x += 1
                            self.rot = 2

                    if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.rot = 2
                    
                elif self.rot == 2:
                    if pl[self.x][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x][self.y-2] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.x += 1
                            self.rot = 3

                    if pl[self.x][self.y-2] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                            self.rot = 3
                    
                elif self.rot == 3:
                    if pl[self.x+1][self.y] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                            self.x += 1
                            self.rot = 0
                    elif pl[self.x-1][self.y-1] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                            self.x -= 1
                            self.rot = 0

                    if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                            self.rot = 0


    def move(self, var):
        if var == 'l':
            if self.rot == 0:
                if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 1:
                if pl[self.x-3][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 2:
                if pl[self.x-2][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 3:
                if pl[self.x-2][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                    pass
                else:
                    self.x -= 1
        else:
            if self.rot == 0:
                if pl[self.x+1][self.y-2] == 1 or pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 1:
                if pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 2:
                if pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y-2] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 3:
                if pl[self.x+2][self.y] == 1 or pl[self.x][self.y-1] == 1:
                    pass
                else:
                    self.x += 1

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            if self.rot == 0:
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x-1][self.y] = 1
            elif self.rot == 1:
                pl[self.x-2][self.y-1] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
            elif self.rot == 2:
                pl[self.x][self.y-2] = 1
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
            elif self.rot == 3:
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
            
        if self.rot == 0:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x-1][self.y] = 1
        elif self.rot == 1:
            if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x-2][self.y-1] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
        elif self.rot == 2:
            if pl[self.x][self.y-1] == 1 or pl[self.x-1][self.y+1] == 1:
                self.mov = False
                pl[self.x][self.y-2] = 1
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
        elif self.rot == 3:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1 or pl[self.x+1][self.y+1] == 1:
                self.mov = False
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1


    def colors(self, clt):
        if self.rot == 0:
            clt[self.x][self.y-2] = DEEP_BLUE
            clt[self.x][self.y-1] = DEEP_BLUE
            clt[self.x][self.y] = DEEP_BLUE
            clt[self.x-1][self.y] = DEEP_BLUE
        elif self.rot == 1:
            clt[self.x-2][self.y-1] = DEEP_BLUE
            clt[self.x-1][self.y-1] = DEEP_BLUE
            clt[self.x][self.y-1] = DEEP_BLUE
            clt[self.x][self.y] = DEEP_BLUE
        elif self.rot == 2:
            clt[self.x][self.y-2] = DEEP_BLUE
            clt[self.x-1][self.y-2] = DEEP_BLUE
            clt[self.x-1][self.y-1] = DEEP_BLUE
            clt[self.x-1][self.y] = DEEP_BLUE
        elif self.rot == 3:
            clt[self.x-1][self.y-1] = DEEP_BLUE
            clt[self.x-1][self.y] = DEEP_BLUE
            clt[self.x][self.y] = DEEP_BLUE
            clt[self.x+1][self.y] = DEEP_BLUE


    def show(self, plansza):
        if self.rot == 0:
            pygame.draw.rect(plansza, DEEP_BLUE, (self.x*bok, (self.y-2)*bok, bok, 3*bok))
            pygame.draw.rect(plansza, DEEP_BLUE, ((self.x-1)*bok, self.y*bok, bok, bok))
        elif self.rot == 1:
            pygame.draw.rect(plansza, DEEP_BLUE, (self.x*bok, self.y*bok, bok, bok))
            pygame.draw.rect(plansza, DEEP_BLUE, ((self.x-2)*bok, (self.y-1)*bok, 3*bok, bok))
        elif self.rot == 2:
            pygame.draw.rect(plansza, DEEP_BLUE, (self.x*bok, (self.y-2)*bok, bok, bok))
            pygame.draw.rect(plansza, DEEP_BLUE, ((self.x-1)*bok, (self.y-2)*bok, bok, 3*bok))
        elif self.rot == 3:
            pygame.draw.rect(plansza, DEEP_BLUE, ((self.x-1)*bok, (self.y-1)*bok, bok, 2*bok))
            pygame.draw.rect(plansza, DEEP_BLUE, (self.x*bok, self.y*bok, 2*bok, bok))

class S(tetr):
    def change(self, var):
        if self.mov:
            self.rot += 1
            if self.rot == 4:
                self.rot = 0
            if self.rot == 0 or self.rot == 2: 
                if pl[self.x-1][self.y] == 1:
                    self.x += 1
                    if pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y-1] == 1:
                        self.x -= 1
                        self.rot = 1
                elif pl[self.x+1][self.y-1] == 1:
                    self.x -= 1
                    if pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y-1] == 1:
                        self.x += 1
                        self.rot = 1

                if pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y-1] == 1:
                        self.rot = 1
                
            else:
                if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1:
                    self.x += 1
                    if pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1:
                        self.x -= 1
                        self.rot = 0

                if pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1:
                        self.rot = 0
            

    def move(self, var):
        if var == 'l':
            if self.rot == 0 or self.rot == 2:
                if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                    pass
                else:
                    self.x -= 1
            else:
                if pl[self.x-1][self.y] == 1 or pl[self.x-2][self.y-2] == 1 or pl[self.x-2][self.y-1] == 1:
                    pass
                else:
                    self.x -= 1
        else:
            if self.rot == 0 or self.rot == 2:
                if pl[self.x+2][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            else:
                if pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1 or pl[self.x][self.y-2] == 1:
                    pass
                else:
                    self.x += 1

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            if self.rot == 0 or self.rot == 2:
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y-1] = 1
            else:
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
        if self.rot == 0 or self.rot == 2:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1 or pl[self.x+1][self.y] == 1:
                self.mov = False
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y-1] = 1
        else:
            if pl[self.x-1][self.y] == 1 or pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1

    def colors(self, clt):
        if self.rot == 0 or self.rot == 2:
            clt[self.x-1][self.y] = GREEN
            clt[self.x][self.y-1] = GREEN
            clt[self.x][self.y] = GREEN
            clt[self.x+1][self.y-1] = GREEN
        else:
            clt[self.x][self.y-1] = GREEN
            clt[self.x][self.y] = GREEN
            clt[self.x-1][self.y-2] = GREEN
            clt[self.x-1][self.y-1] = GREEN

    def show(self, plansza):
        if self.rot == 0 or self.rot == 2:
            pygame.draw.rect(plansza, GREEN, (self.x*bok, (self.y-1)*bok, 2*bok, bok))
            pygame.draw.rect(plansza, GREEN, ((self.x-1)*bok, self.y*bok, 2*bok, bok))
        else:
            pygame.draw.rect(plansza, GREEN, (self.x*bok, (self.y-1)*bok, bok, 2*bok))
            pygame.draw.rect(plansza, GREEN, ((self.x-1)*bok, (self.y-2)*bok, bok, 2*bok))

class Z(tetr):
    def change(self, var):
        if self.mov:
            self.rot += 1
            if self.rot == 4:
                self.rot = 0
            if self.rot == 0 or self.rot == 2: 
                if pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                    self.x -= 1
                    if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                        self.x += 1
                        self.rot = 1

                if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1:
                        self.rot = 1
                
                
            else:
                if pl[self.x-1][self.y] == 1 or pl[self.x][self.y-2] == 1:
                    self.x += 1
                    if pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1:
                        self.x -= 1
                        self.rot = 0

                if pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1:
                        self.rot = 0

    def move(self, var):
        if var == 'l':
            if self.rot == 0 or self.rot == 2:
                if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            else:
                if pl[self.x-1][self.y-2] == 1 or pl[self.x-2][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                    pass
                else:
                    self.x -= 1
        else:
            if self.rot == 0 or self.rot == 2:
                if pl[self.x+2][self.y] == 1 or pl[self.x+1][self.y-1] == 1:
                    pass
                else:
                    self.x += 1
            else:
                if pl[self.x+1][self.y-2] == 1 or pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y] == 1:
                    pass
                else:
                    self.x += 1

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            if self.rot == 0 or self.rot == 2:
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
            else:
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x-1][self.y-1] = 1
        if self.rot == 0 or self.rot == 2:
            if pl[self.x+1][self.y+1] == 1 or pl[self.x][self.y+1] == 1 or pl[self.x-1][self.y] == 1:
                self.mov = False
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
        else:
            if pl[self.x][self.y] == 1 or pl[self.x-1][self.y+1] == 1:
                self.mov = False
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x-1][self.y-1] = 1

    def colors(self, clt):
        if self.rot == 0 or self.rot == 2:
            clt[self.x-1][self.y-1] = RED
            clt[self.x][self.y-1] = RED
            clt[self.x][self.y] = RED
            clt[self.x+1][self.y] = RED
        else:
            clt[self.x][self.y-2] = RED
            clt[self.x][self.y-1] = RED
            clt[self.x-1][self.y] = RED
            clt[self.x-1][self.y-1] = RED


    def show(self, plansza):
        if self.rot == 0 or self.rot == 2:
            pygame.draw.rect(plansza, RED, ((self.x-1)*bok, (self.y-1)*bok, 2*bok, bok))
            pygame.draw.rect(plansza, RED, (self.x*bok, self.y*bok, 2*bok, bok))
        else:
            pygame.draw.rect(plansza, RED, (self.x*bok, (self.y-2)*bok, bok, 2*bok))
            pygame.draw.rect(plansza, RED, ((self.x-1)*bok, (self.y-1)*bok, bok, 2*bok))

class T(tetr):
    def change(self, var):
        if self.mov:
            if var == 0:
                self.rot += 1
                if self.rot == 4:
                    self.rot = 0
                if self.rot == 0: 
                    if pl[self.x+1][self.y-1] == 1:
                        self.x -= 1
                        if pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                            self.x += 1
                            self.rot = 3

                    if pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                            self.rot = 3

                elif self.rot == 1:
                    if pl[self.x-1][self.y] == 1 or pl[self.x-1][self.y-2] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x -= 1
                            self.rot = 0

                    if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.rot = 0
                    
                elif self.rot == 2:
                    if pl[self.x+1][self.y] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x += 1
                            self.rot = 1

                    if pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.rot = 1
                    
                elif self.rot == 3:
                    if pl[self.x-1][self.y-1] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x -= 1
                            self.rot = 2

                    elif pl[self.x][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x += 1
                            self.rot = 2

                    if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.rot = 2

                        

            else:
                self.rot -= 1
                if self.rot == -1:
                    self.rot = 3
                if self.rot == 0: 
                    if pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y] == 1:
                        self.x -= 1
                        if pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                            self.x += 1
                            self.rot = 1

                    if pl[self.x+1][self.y-1] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                            self.rot = 1
                    

                elif self.rot == 1:
                    if pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y-2] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x -= 1
                            self.rot = 2

                    if pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y-1] == 1 or pl[self.x-1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.rot = 2
                    
                elif self.rot == 2:
                    if pl[self.x+1][self.y] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x += 1
                            self.rot = 3

                    elif pl[self.x-1][self.y] == 1:
                        self.x += 1
                        if pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.x -= 1
                            self.rot = 3

                    if pl[self.x-1][self.y] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y] == 1 or pl[self.x][self.y-1] == 1:
                            self.rot = 3
                    
                elif self.rot == 3:
                    if pl[self.x][self.y-2] == 1:
                        self.x -= 1
                        if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.x += 1
                            self.rot = 0

                    if pl[self.x-1][self.y-1] == 1 or pl[self.x][self.y-2] == 1 or pl[self.x][self.y-1] == 1 or pl[self.x][self.y] == 1:
                            self.rot = 0
                    



    def move(self, var):
        if var == 'l':
            if self.rot == 0:
                if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 1:
                if pl[self.x-2][self.y-2] == 1 or pl[self.x-2][self.y-1] == 1 or pl[self.x-2][self.y] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 2:
                if pl[self.x-2][self.y] == 1 or pl[self.x-1][self.y-1] == 1:
                    pass
                else:
                    self.x -= 1
            elif self.rot == 3:
                if pl[self.x-2][self.y-1] == 1 or pl[self.x-1][self.y-2] == 1 or pl[self.x-1][self.y] == 1:
                    pass
                else:
                    self.x -= 1
        else:
            if self.rot == 0:
                if pl[self.x+2][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 1:
                if pl[self.x][self.y-2] == 1 or pl[self.x][self.y] == 1 or pl[self.x+1][self.y-1] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 2:
                if pl[self.x+2][self.y] == 1 or pl[self.x+1][self.y-1] == 1:
                    pass
                else:
                    self.x += 1
            elif self.rot == 3:
                if pl[self.x+1][self.y-2] == 1 or pl[self.x+1][self.y-1] == 1 or pl[self.x+1][self.y] == 1:
                    pass
                else:
                    self.x += 1

    def place(self, pl):
        if self.y == 20:
            self.mov = False
            if self.rot == 0:
                pl[self.x+1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x-1][self.y-1] = 1
            elif self.rot == 1:
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y-1] = 1
            elif self.rot == 2:
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
                pl[self.x][self.y-1] = 1
            elif self.rot == 3:
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
            
        if self.rot == 0:
            if pl[self.x-1][self.y] == 1 or pl[self.x][self.y+1] == 1 or pl[self.x+1][self.y] == 1:
                self.mov = False
                pl[self.x+1][self.y-1] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1
                pl[self.x-1][self.y-1] = 1
        elif self.rot == 1:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y] == 1:
                self.mov = False
                pl[self.x-1][self.y-2] = 1
                pl[self.x-1][self.y-1] = 1
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y-1] = 1
        elif self.rot == 2:
            if pl[self.x-1][self.y+1] == 1 or pl[self.x][self.y+1] == 1 or pl[self.x+1][self.y+1] == 1:
                self.mov = False
                pl[self.x-1][self.y] = 1
                pl[self.x][self.y] = 1
                pl[self.x+1][self.y] = 1
                pl[self.x][self.y-1] = 1
        elif self.rot == 3:
            if pl[self.x-1][self.y] == 1 or pl[self.x][self.y+1] == 1:
                self.mov = False
                pl[self.x-1][self.y-1] = 1
                pl[self.x][self.y-2] = 1
                pl[self.x][self.y-1] = 1
                pl[self.x][self.y] = 1

    def colors(self, clt):
        if self.rot == 0:
            clt[self.x+1][self.y-1] = PURPLE
            clt[self.x][self.y-1] = PURPLE
            clt[self.x][self.y] = PURPLE
            clt[self.x-1][self.y-1] = PURPLE
        elif self.rot == 1:
            clt[self.x-1][self.y-2] = PURPLE
            clt[self.x-1][self.y-1] = PURPLE
            clt[self.x-1][self.y] = PURPLE
            clt[self.x][self.y-1] = PURPLE
        elif self.rot == 2:
            clt[self.x-1][self.y] = PURPLE
            clt[self.x][self.y] = PURPLE
            clt[self.x+1][self.y] = PURPLE
            clt[self.x][self.y-1] = PURPLE
        elif self.rot == 3:
            clt[self.x-1][self.y-1] = PURPLE
            clt[self.x][self.y-2] = PURPLE
            clt[self.x][self.y-1] = PURPLE
            clt[self.x][self.y] = PURPLE


    def show(self, plansza):
        if self.rot == 0:
            pygame.draw.rect(plansza, PURPLE, ((self.x-1)*bok, (self.y-1)*bok, 3*bok, bok))
            pygame.draw.rect(plansza, PURPLE, (self.x*bok, self.y*bok, bok, bok))
        elif self.rot == 1:
            pygame.draw.rect(plansza, PURPLE, (self.x*bok, (self.y-1)*bok, bok, bok))
            pygame.draw.rect(plansza, PURPLE, ((self.x-1)*bok, (self.y-2)*bok, bok, 3*bok))
        elif self.rot == 2:
            pygame.draw.rect(plansza, PURPLE, (self.x*bok, (self.y-1)*bok, bok, bok))
            pygame.draw.rect(plansza, PURPLE, ((self.x-1)*bok, self.y*bok, 3*bok, bok))
        elif self.rot == 3:
            pygame.draw.rect(plansza, PURPLE, ((self.x-1)*bok, (self.y-1)*bok, bok, bok))
            pygame.draw.rect(plansza, PURPLE, (self.x*bok, (self.y-2)*bok, bok, 3*bok))
        
            



#deklaracje
pl = []
clt = []
for x in range(0, 12):
    pl.append([])
    clt.append([])
    for y in range(0, 23):
        if x == 0 or x == 11:
            pl[x].append(1)
        else:
            pl[x].append(0)
        clt[x].append(BLACK)

const_period = 50
period = const_period
licznik = 0
score = 0
last_score = 0


wyb = random.choice(['I', 'O', 'L', 'J', 'S', 'Z', 'T'])
x = 5
r = random.randint(0, 3)
if wyb == 'I':
    tetr = I(x, -2, r)
if wyb == 'O':
    tetr = O(x, -2, r)
if wyb == 'L':
    tetr = L(x, -2, r)
if wyb == 'J':
    tetr = J(x, -2, r)
if wyb == 'S':
    tetr = S(x, -2, r)
if wyb == 'Z':
    tetr = Z(x, -2, r)
if wyb == 'T':
    tetr = T(x, -2, r)


while True:
    #wyglad planszy
    for x in range(0, 12):
        for y in range(0, 23):
            pygame.draw.rect(plansza, clt[x][y], (x*bok, y*bok, bok, bok))

    pygame.draw.rect(plansza, GRAY, (0, 0, bok, 22*bok))
    pygame.draw.rect(plansza, GRAY, (11*bok, 0, bok, 22*bok))
    pygame.draw.rect(plansza, GRAY, (0, 0, 12*bok, bok))
    pygame.draw.rect(plansza, GRAY, (0, 21*bok, 12*bok, bok))

    #obsluga klockow
    tetr.show(plansza)
    tetr.place(pl)
    if licznik % period == 0 and tetr.mov == True:
        tetr.y += 1

    #przyspieszanie
    if score == last_score + 50:
        const_period -= 5


    #generowanie nowych klockow
    k = False
    if tetr.mov:
        k = True

    if k == False:
        tetr.colors(clt)
        period = const_period
        score += 5
        wyb = random.choice(['I', 'O', 'L', 'J', 'S', 'Z', 'T'])
        x = 5
        r = random.randint(0, 3)
        if wyb == 'I':
            tetr = I(x, -2, r)
        if wyb == 'O':
            tetr = O(x, -2, r)
        if wyb == 'L':
            tetr = L(x, -2, r)
        if wyb == 'J':
            tetr = J(x, -2, r)
        if wyb == 'S':
            tetr = S(x, -2, r)
        if wyb == 'Z':
            tetr = Z(x, -2, r)
        if wyb == 'T':
            tetr = T(x, -2, r)

    #usuwanie linii
    for y in range(0, 23):
        var = True
        for x in range(1, 10):
            if pl[x][y] == 0:
                var = False
        if var:
            score += 10
            for x in range(1, 10):
                for yi in range(y-1, 0, -1):
                    pl[x][yi+1] = pl[x][yi]
                    clt[x][yi+1] = clt[x][yi]
                    pl[x][yi] = 0
                    pl[x][yi] = BLACK
                    
    #spojnosc tablic
    for x in range(1, 10):
        for y in range(0, 23):
            if clt[x][y] != BLACK:
                pl[x][y] = 1

    
    #warunki przegranej
    var = False
    for x in range(1, 10):
        if pl[x][0] == 1:
            var = True
    if var:
        break
                    

        

    #obsluga zdarzen/sterowanie
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_q:
                tetr.change(0)
            elif event.key == K_w:
                tetr.change(1)
            if event.key == K_LEFT:
                tetr.move('l')
            elif event.key == K_RIGHT:
                tetr.move('r')
            elif event.key  == K_DOWN:
                period = 5

        if event.type == KEYUP:
            if event.key  == K_DOWN:
                period = const_period
    

    licznik += 1

    if licznik % 1000 == 0:
        licznik = 0

    pygame.display.update()
    zegar.tick(FPS)


   
    
    







    
