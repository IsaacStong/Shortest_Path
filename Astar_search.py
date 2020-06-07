"""Created by Isaac Stong on 6/6/20
    This file creates a path using Astar"""
from Node import Node

maze = []

def Astar_path(board, start, end):
    #Node initialization
    start_Node = Node(None, start)
    start_Node.find_heuristic(end)
    end_Node = Node(None, end)
    #List initialization
    open_List = []
    closed_List = []

    open_List.append(start_Node)
    current_Node = start_Node

    #While loop keeps track of
    while open_List is not None:
        children = current_Node.find_children(maze, end_Node)
        for i in len(children):
            if children[i].f_value < current_Node.f_value:
                open_List.append(children[i])

