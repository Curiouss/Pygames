# -coding:utf8- --

import pygame
from pygame.locals import *
from random import randint
from sys import exit
import random
import time
from copy import deepcopy

"""
tpye 1: oo type2: ooo tpye3:  oo tpye4: oooo type5 ooo type6: oo  type7: ooo
        oo        o          oo                      o         oo         o
"""

class Const1(object):
    def __init__(self):
        self.SPosition=[[56,14],[70,14],[56,28],[70,28]]
        self.color=(0,255,0)
        self.typeNum=1
        self.form=0
        self.col=[14,28, 42, 56, 70, 84, 98, 112]
        self.row=[280, 266, 252, 238, 224, 210, 196, 182, 168, 154, 140, 126, 112, 98, 84, 70, 56, 42, 28, 14]
        self.White=pygame.Surface((14,14))
        self.Red = pygame.Surface((14, 14))
        self.Red.fill((255,0,0))
    def position(self):
        return self.SPosition
    def type(self,typeNum):
        if typeNum==1:
            self.SPosition = [[56,14],[70,14],[56,28],[70,28]]
        elif typeNum==2:
            self.SPosition = [[56,14],[70,14],[56,28],[84,14]]
        elif typeNum==3:
            self.SPosition = [[56,14],[70,14],[70,28],[84,28]]
        elif typeNum==4:
            self.SPosition = [[42,14],[56,14],[70,14],[84,14]]
        elif typeNum==5:
            self.SPosition = [[42,14],[56,14],[70,14],[70,28]]
        elif typeNum==6:
            self.SPosition = [[56,28],[70,14],[70,28],[84,14]]
        elif typeNum==7:
            self.SPosition = [[56,14],[70,14],[42,14],[56,28]]
        #self.SPosition=sorted(self.SPosition)
        self.typeNum=typeNum
        self.form=0
        print self.typeNum
    #def color(self,typeColor):
    def clearcheck(self,SC):
        for i in self.row:
            linecount=0
            for j in self.col:
                if SC.get_at((j,i))==(255, 0, 0):
                    linecount+=1
            if linecount==8:
                self.White.fill((255,255,255))
                for k in self.col:
                    SC.blit(self.White,(k,i))
                pygame.display.update()
                pygame.time.delay(50)
                self.White.fill((255,0,0))
                for k in self.col:
                    SC.blit(self.White,(k,i))
                pygame.display.update()
                pygame.time.delay(50)
                self.White.fill((255,255,255))
                for k in self.col:
                    SC.blit(self.White,(k,i))
                pygame.display.update()
                pygame.time.delay(50)
                l=20-i//14
                for m in self.row[l+1:]:
                    for n in self.col:
                        if SC.get_at((n,m))==(255, 0, 0):
                            SC.blit(self.Red, (n,m+14))
                        elif SC.get_at((n,m))==(255, 255, 255):
                            SC.blit(self.White, (n, m + 14))
                pygame.display.update()



    def ChangeDire(self):
        return self.direction
    def drop(self,Coords):
        CoordNew=[]
        for i in range(len(Coords)):
            CoordNew.append((Coords[i][0],Coords[i][1]+14))
        return CoordNew
    def left(self,Coords):
        CoordNew=[]
        for i in range(len(Coords)):
            CoordNew.append((Coords[i][0]-14,Coords[i][1]))
        return CoordNew
    def right(self,Coords):
        CoordNew=[]
        for i in range(len(Coords)):
            CoordNew.append((Coords[i][0]+14,Coords[i][1]))
        return CoordNew
    def Change(self,Coords):
        if self.typeNum==1:
            self.SPosition=Coords
        if self.typeNum==2:
            if self.form==0:
                CoordNew=[(Coords[1][0]-14, Coords[1][1]),(Coords[1][0] , Coords[1][1]),
                          (Coords[1][0]-28, Coords[1][1]),(Coords[1][0] , Coords[1][1]-14)]
                self.SPosition=CoordNew
                self.form=1
            elif self.form==1:
                CoordNew=[(Coords[1][0]+14, Coords[1][1]),(Coords[1][0] , Coords[1][1]),
                          (Coords[1][0] , Coords[1][1]-14),(Coords[1][0] , Coords[1][1]-28)]
                self.SPosition = CoordNew
                self.form=2
            elif self.form==2:
                CoordNew=[(Coords[1][0]+28,Coords[1][1]),(Coords[1][0],Coords[1][1]),
                          (Coords[1][0]+14,Coords[1][1]),(Coords[1][0],Coords[1][1]+14)]
                self.SPosition=CoordNew
                self.form=3
            elif self.form==3:
                CoordNew=[(Coords[1][0]-14,Coords[1][1]),(Coords[1][0],Coords[1][1]),
                          (Coords[1][0],Coords[1][1]+28),(Coords[1][0],Coords[1][1]+14)]
                self.SPosition=CoordNew
                self.form=0

        if self.typeNum == 5:
            if self.form == 0:
                CoordNew = [(Coords[2][0]-14, Coords[2][1]), (Coords[2][0], Coords[2][1]-14),
                            (Coords[2][0], Coords[2][1]), (Coords[2][0], Coords[2][1]-28)]
                self.SPosition = CoordNew
                self.form = 1
            elif self.form == 1:
                CoordNew = [(Coords[2][0], Coords[2][1]-14), (Coords[2][0], Coords[2][1]),
                            (Coords[2][0]+14, Coords[2][1]), (Coords[2][0]+28, Coords[2][1])]
                self.SPosition = CoordNew
                self.form = 2
            elif self.form == 2:
                CoordNew = [(Coords[2][0]+14, Coords[2][1]), (Coords[2][0], Coords[2][1]+14),
                            (Coords[2][0], Coords[2][1]), (Coords[2][0], Coords[2][1]+28)]
                self.SPosition = CoordNew
                self.form = 3
            elif self.form == 3:
                CoordNew = [(Coords[2][0]-14, Coords[2][1]), (Coords[2][0]-28, Coords[2][1]),
                            (Coords[2][0], Coords[2][1]), (Coords[2][0], Coords[2][1]+14)]
                self.SPosition = CoordNew
                self.form = 0
        if self.typeNum == 7:
            if self.form == 0:
                CoordNew = [(Coords[0][0], Coords[0][1]), (Coords[0][0]+14, Coords[0][1]),
                            (Coords[0][0], Coords[0][1]-14), (Coords[0][0], Coords[0][1]+14)]
                self.SPosition = CoordNew
                self.form = 1
            elif self.form == 1:
                CoordNew = [(Coords[0][0], Coords[0][1]), (Coords[0][0]+14, Coords[0][1]),
                            (Coords[0][0], Coords[0][1]-14), (Coords[0][0]-14, Coords[0][1])]
                self.SPosition = CoordNew
                self.form = 2
            elif self.form == 2:
                CoordNew = [(Coords[0][0], Coords[0][1]), (Coords[0][0]-14, Coords[0][1]),
                            (Coords[0][0], Coords[0][1]+14), (Coords[0][0], Coords[0][1]-14)]
                self.SPosition = CoordNew
                self.form = 3
            elif self.form == 3:
                CoordNew = [(Coords[0][0], Coords[0][1]), (Coords[0][0]-14, Coords[0][1]),
                            (Coords[0][0], Coords[0][1]+14), (Coords[0][0]+14, Coords[0][1])]
                self.SPosition = CoordNew
                self.form = 0
        if self.typeNum == 4:
            if self.form == 0:
                CoordNew = [(Coords[1][0], Coords[1][1]-14), (Coords[1][0], Coords[1][1]),
                            (Coords[1][0], Coords[1][1]+14), (Coords[1][0], Coords[1][1]+28)]
                self.SPosition = CoordNew
                self.form = 1
            elif self.form == 1:
                CoordNew = [(Coords[1][0]-14, Coords[1][1]), (Coords[1][0], Coords[1][1]),
                            (Coords[1][0]+14, Coords[1][1]), (Coords[1][0]+28, Coords[1][1])]
                self.SPosition = CoordNew
                self.form = 0
        if self.typeNum == 3:
            if self.form == 0:
                CoordNew = [(Coords[1][0], Coords[1][1]-14), (Coords[1][0], Coords[1][1]),
                            (Coords[1][0]-14, Coords[1][1]), (Coords[1][0]-14, Coords[1][1]+14)]
                self.SPosition = CoordNew
                self.form = 1
            elif self.form == 1:
                CoordNew = [(Coords[1][0]-14, Coords[1][1]), (Coords[1][0], Coords[1][1]),
                            (Coords[1][0], Coords[1][1]+14), (Coords[1][0]+14, Coords[1][1]+14)]
                self.SPosition = CoordNew
                self.form = 0
        if self.typeNum == 6:
            if self.form == 1:
                CoordNew = [(Coords[1][0]+14, Coords[1][1]), (Coords[1][0], Coords[1][1]),
                            (Coords[1][0]-14, Coords[1][1]+14), (Coords[1][0], Coords[1][1]+14)]
                self.SPosition = CoordNew
                self.form = 0
            elif self.form == 0:
                CoordNew = [(Coords[1][0]-14, Coords[1][1]), (Coords[1][0], Coords[1][1]),
                            (Coords[1][0]-14, Coords[1][1]-14), (Coords[1][0], Coords[1][1]+14)]
                self.SPosition = CoordNew
                self.form = 1

class Background(object):
    def __init__(self):
        self.screen=pygame.display.set_mode((140, 308), RESIZABLE, 32)
        self.title=pygame.display.set_caption("MYSNAKEGAME")
        self.square=pygame.Surface((14,14))
    def Bg(self):
        return self.screen
    def Ttl(self):
        return self.title
    def Squ(self):
        return self.square
    def Round(self):
        Coords = []
        for i in range(10):
            i=i*14
            Coords.append((i,0))
            Coords.append((i,294))

        for j in range(21)*14:
            j=j*14
            Coords.append((0,j))
            Coords.append((126,j))
        return Coords


def MainGame():

    pygame.init()
    SCR = Background()
    screen=SCR.Bg()
    screen.fill((255, 255, 255))
    SCR.Ttl()
    square=SCR.square
    square.fill((255, 215, 0))
    RdCoor=SCR.Round()
    for i in RdCoor:
        screen.blit(square,i)
    pygame.display.update()
    con_direction = '0'
    moveflag=0
    moveflag2=0
    C1 = Const1()
    C1.type(7)
    #C1.type(randint(1,7))
    Drop = square
    DropDark = square
    DropRed =square
    Drop.fill((0, 255, 0))
    Drop_Position = C1.SPosition
    for i in Drop_Position:
        screen.blit(Drop, i)
    pygame.display.update()
    pygame.time.delay(200)

    paused=False

    while True:
        looptime=0
        while looptime<3:
            for event in pygame.event.get():
                if event.type == QUIT:
                    print "quit"
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        con_direction = '3'
                    elif event.key == K_DOWN:
                        continue
                        #faster
                    elif event.key == K_LEFT:
                        con_direction = '1'
                    elif event.key == K_RIGHT:
                        con_direction = '2'
                    elif event.key == K_SPACE:
                        print "not"*paused,"paused"
                        paused = not paused
            if paused:
                continue
            pygame.time.delay(50)
            #print con_direction
            if con_direction == '0':
                for i in range(4):
                    A = screen.get_at((Drop_Position[i][0], Drop_Position[i][1] + 14))
                    B = screen.get_at((Drop_Position[i][0]-14, Drop_Position[i][1]))
                    C = screen.get_at((Drop_Position[i][0]+14, Drop_Position[i][1]))
                    if A != (255, 255, 255, 255) and A != (0, 255, 0, 255):
                        DropRed.fill((255, 0, 0))
                        for i in Drop_Position:
                            screen.blit(DropRed, i)
                        pygame.time.delay(0)
                        C1.type(randint(1, 7))
                        C1.clearcheck(screen)
                        C1.clearcheck(screen)
                        C1.clearcheck(screen)
                        C1.clearcheck(screen)
                        Drop_Position = C1.SPosition
            elif con_direction == '1':
                    moveflag2=0
                    for i in range(4):
                        if screen.get_at((Drop_Position[i][0]-14,Drop_Position[i][1]))==(255, 255, 255, 255) or screen.get_at((Drop_Position[i][0]-14,Drop_Position[i][1]))==(0, 255, 0, 255):
                            moveflag2+=1
                    if moveflag2==4:
                        DropDark.fill((255, 255, 255))
                        for i in Drop_Position:
                            screen.blit(DropDark, i)
                        Drop_Position = C1.left(Drop_Position)
                        moveflag2=99999
                        con_direction = '0'
                        pygame.display.update()

            elif con_direction == '2':
                    moveflag2 = 0
                    for i in range(4):
                        if screen.get_at((Drop_Position[i][0]+14,Drop_Position[i][1])) == (255, 255, 255, 255) or screen.get_at((Drop_Position[i][0]+14,Drop_Position[i][1])) == (0, 255, 0, 255):
                            moveflag2 += 1
                    if moveflag2 == 4:
                        DropDark.fill((255, 255, 255))
                        for i in Drop_Position:
                            screen.blit(DropDark, i)
                        Drop_Position = C1.right(Drop_Position)
                        moveflag2=99999
                        con_direction = '0'
                        pygame.display.update()
            elif con_direction == '3':
                DropDark.fill((255, 255, 255))
                for i in Drop_Position:
                    screen.blit(DropDark, i)
                C1.Change(Drop_Position)
                Drop_Position=C1.SPosition
                Drop.fill((0, 255, 0))
                for i in Drop_Position:
                    screen.blit(Drop, i)
                con_direction = '0'
                pygame.display.update()
            looptime+=1
        for i in range(4):
            A = screen.get_at((Drop_Position[i][0], Drop_Position[i][1] + 14))
            B = screen.get_at((Drop_Position[i][0] - 14, Drop_Position[i][1]))
            C = screen.get_at((Drop_Position[i][0] + 14, Drop_Position[i][1]))
            #print A,B,C
            if A != (255, 255, 255, 255) and A != (0, 255, 0, 255):
                DropRed.fill((255, 0, 0))
                for i in Drop_Position:
                    screen.blit(DropRed, i)
                pygame.time.delay(0)
                C1.type(randint(1,7))
                C1.clearcheck(screen)
                C1.clearcheck(screen)
                C1.clearcheck(screen)
                C1.clearcheck(screen)
                Drop_Position = C1.SPosition
        DropDark.fill((255, 255, 255))
        for i in Drop_Position:
            screen.blit(DropDark, i)
        Drop_Position=C1.drop(Drop_Position)
        Drop.fill((0, 255, 0))
        for i in Drop_Position:
            screen.blit(Drop, i)
        pygame.display.update()
        for i in range(4):
            A = screen.get_at((Drop_Position[i][0], Drop_Position[i][1] + 14))
            B = screen.get_at((Drop_Position[i][0] - 14, Drop_Position[i][1]))
            C = screen.get_at((Drop_Position[i][0] + 14, Drop_Position[i][1]))
            if A != (255, 255, 255, 255) and A != (0, 255, 0, 255):
                DropRed.fill((255, 0, 0))
                for i in Drop_Position:
                    screen.blit(DropRed, i)
                pygame.time.delay(0)
                C1.type(randint(1, 7))
                C1.clearcheck(screen)
                C1.clearcheck(screen)
                C1.clearcheck(screen)
                C1.clearcheck(screen)
                Drop_Position = C1.SPosition
        pygame.time.delay(0)

if __name__ == '__main__':
    MainGame()