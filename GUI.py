"""Created by Isaac Stong 6/8/20
    GUI for pathfinding"""
import pygame as pg
import tkinter as tk
from Astar_search import Astar_path

pg.init()

#Important Variables
App_Height = 700
App_Width = 700
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (150, 50, 50)
blockSize = 14

#create screen view
screen = pg.display.set_mode((App_Height, App_Width))
screen.fill(White)

#Title and features
pg.display.set_caption("A* Pathfinder")
icon = pg.image.load("monitor.png")
pg.display.set_icon(icon)


#Draws boxes
def drawGrid():
    for x in range(App_Width//blockSize):
        for y in range(App_Height//blockSize):
            rect = pg.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pg.draw.rect(screen, Black, rect, 1)


#Draws beginning and end points
def draw_Start_and_Goal(start, goal):
    pg.draw.rect(screen, Red, (start[0]*blockSize, start[1]*blockSize, blockSize-1, blockSize-1))
    pg.draw.rect(screen, Red, (goal[0] * blockSize, goal[1] * blockSize, blockSize-1, blockSize-1))


#Draw Path
def draw_path(path):
    for box in path:
        pg.draw.rect(screen, Red, (box[0]*blockSize, box[1]*blockSize, blockSize-1, blockSize-1))


def main():
    #Initialize maze
    maze = [0 for i in range(50)]
    for i in range(50):
        maze[i] = [0 for j in range(50)]

    path = Astar_path(maze, (0, 0), (37, 44))
    draw_path(path)


#Loop runs application window
running = True
while running:
    drawGrid()
    main()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()
