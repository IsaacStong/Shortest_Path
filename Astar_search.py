"""Created by Isaac Stong on 6/6/20
    This file creates a path using Astar"""
from Node import Node


def Astar_path(maze, start, end):
    #Node initialization
    start_Node = Node(None, start)
    start_Node.find_heuristic(end)
    start_Node.f_value = start_Node.g_value + start_Node.h_value
    end_Node = Node(None, end)
    #List initialization
    #Holds Nodes that need to be explored
    open_List = []
    #Holds solution
    closed_List = []

    open_List.append(start_Node)
    current_Node = start_Node

    #While loop keeps track of open_list
    while open_List is not None:
        children = current_Node.find_children(maze, end_Node)
        for i in range(len(children)):
            tem = children[i].f_value
            temp = current_Node.f_value
            if children[i].f_value < current_Node.f_value:
                open_List.append(children[i])
        open_List.pop(0)
        maze[current_Node.position[0]][current_Node.position[1]] = 2
        current_Node = open_List[0]

        if current_Node.position == end_Node.position:
            maze[end_Node.position[0]][end_Node.position[1]] = 2
            return maze


sample_maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],]
solved_sample = Astar_path(sample_maze, (1, 1), (8, 7))
print((solved_sample))