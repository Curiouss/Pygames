# -coding:utf8- --

import pygame
from pygame.locals import *
from random import randint
from sys import exit
import random

#from copy import deepcopy

class Snake(object):
    def __init__(self):
        self.SPosition=[[0,0]]
        self.direction='2'
    def postion(self):
        return self.SPosition
    def ChangeDire(self):
        return self.direction
    def SnakeControl(self):
        #SnakeLen=len(self.SPosition)-1

        #The postion direction 1:up 2:down 3:left 4:right
        if self.direction == '1':
            self.SPosition[0][0] += 14
        elif self.direction == '2':
            self.SPosition[0][0] -= 14
        elif self.direction == '3':
            self.SPosition[0][1] -= 14
        elif self.direction == '4':
            self.SPosition[0][1] += 14
    def Eat(self,FPosition):
        self.SPosition.insert(0, FPosition)
    def AppleRefresh(self):
        return (random.randint(1, 39) * 14, random.randint(1, 39) * 14)

def MainGame():
    pygame.init()
    screen = pygame.display.set_mode((560,560), RESIZABLE, 32)
    pygame.display.set_caption("MYSNAKEGAME")
    snake = Snake()
    snake_direction = snake.ChangeDire()
    snake_position = snake.postion()
    Apple = pygame.Surface((14, 14))
    AppleCoord=snake.AppleRefresh()
    Apple.fill((255, 248, 220))
    Position = []
    Count=-1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print "quit"
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if snake_direction == '2':
                        break
                    snake_direction = '1'
                elif event.key == K_DOWN:
                    if snake_direction == '1':
                        break
                    snake_direction = '2'
                elif event.key == K_LEFT:
                    if snake_direction == '4':
                        break
                    snake_direction = '3'
                elif event.key == K_RIGHT:
                    if snake_direction == '3':
                        break
                    snake_direction = '4'
                elif event.key == K_SPACE:
                    AppleCoord = snake.AppleRefresh()
        screen.fill((100, 100, 100))
        Position.append(1*snake_position[-1])
        Position=Position[Count:]
        for pos in Position:
            temp_rect = pygame.Rect(pos[0],pos[1],14,14)
            pygame.draw.rect(screen, (255, 0, 0), temp_rect)

        screen.blit(Apple, AppleCoord)

        if AppleCoord[0]==snake_position[0][0] and AppleCoord[1]==snake_position[0][1]:
            print "Yes"
            Count-=1
            pygame.time.delay(0)
            AppleCoord = snake.AppleRefresh()
            print AppleCoord, Position

        if snake_direction == '1':
            snake_position[0][1] -= 14
        elif snake_direction == '2':
            snake_position[0][1] += 14
        elif snake_direction == '3':
            snake_position[0][0] -= 14
        elif snake_direction == '4':
            snake_position[0][0] += 14

        if snake_position[0][0] > 546:
            snake_position[0][0] -= 560
        elif snake_position[0][0] < 0:
            snake_position[0][0] += 560
        elif snake_position[0][1] < 0:
            snake_position[0][1] += 560
        elif snake_position[0][1]> 546:
            snake_position[0][1] -= 560

        pygame.time.delay(30)

        if Count<-1:
            if snake_position[0] in Position[1:]:
                pygame.time.delay(20000)
                print "Game Over"

        pygame.display.update()


MainGame()