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
start = ()
goal = ()
obs = []

# Initialize maze
maze = [0 for i in range(50)]
for i in range(50):
    maze[i] = [0 for j in range(50)]

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


def submit():
    global start
    global goal
    st = start_box.get().split(',')
    go = end_box.get().split(',')
    start = (int(st[0]), int(st[1]))
    goal = (int(go[0]), int(go[1]))
    window.quit()
    window.destroy()


#Create user window using tkinter
window = tk.Tk()
label1 = tk.Label(window, text="Start: (x,y)")
start_box = tk.Entry(window)
label2 = tk.Label(window, text="Goal: (x,y)")
end_box = tk.Entry(window)
var = tk.IntVar()
submit = tk.Button(window, text='Submit', command=submit)

submit.grid(columnspan=2, row=3)
label2.grid(row=1, pady=3)
end_box.grid(row=1, column=1, pady=3)
start_box.grid(row=0, column=1, pady=3)
label1.grid(row=0, pady=3)

window.update()
tk.mainloop()


def checkMouse(x):
    global obs
    w = x[0]
    h = x[1]
    h1 = w // (App_Width // 50)
    h2 = h // (App_Height // 50)
    obs.append((h1, h2))
    pg.draw.rect(screen, Black, (h1*blockSize, h2*blockSize, blockSize-1, blockSize-1))

running1 = True
while running1:
    drawGrid()
    draw_Start_and_Goal(start, goal)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running1 = False
        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            checkMouse(pos)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                running1 = False
                break
    pg.display.update()


def main():
    for i in range(len(obs)):
        maze[obs[i][0]][obs[i][1]] = 1
    path = Astar_path(maze, start, goal)
    draw_path(path)


main()
#Loop runs application window
running2 = True
while running2:
    drawGrid()
    pg.draw.rect(screen, Black, (obs[i][0] * blockSize, obs[i][1] * blockSize, blockSize - 1, blockSize - 1))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running2 = False

    pg.display.update()
