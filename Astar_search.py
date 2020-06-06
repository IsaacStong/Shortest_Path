"""Created by Isaac Stong on 6/6/20
    This file creates a path using Astar"""
from Node import Node


def Astar_path(board, start, end):
    #Node initialization
    start_Node = Node(None, start)
    end_Node = Node(None, end)
    #List initialization
    open_List = []
    closed_List = []

    open_List.append(start_Node)

