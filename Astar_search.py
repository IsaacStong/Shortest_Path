"""Created by Isaac Stong on 6/6/20
    This file creates a path using Astar"""
from Node import Node


def Astar_path(maze, start, end):
    #Node and List Initialization
    start_Node = Node(None, start)
    end_Node = Node(None, end)
    open_List = []
    closed_List = []

    #Add starting node to open
    open_List.append(start_Node)

    #While loop goes until end is found
    while len(open_List) > 0:
        #Find next current
        current_Node = open_List[0]
        current_index = 0
        for i, node in enumerate(open_List):
            if node.f_value < current_Node.f_value:
                current_Node = node
                current_index = i

        #Remove the current_Node from open and and append to closed
        open_List.pop(current_index)
        closed_List.append(current_Node)

        #Test for and return goal
        if current_Node.position == end_Node.position:
            path = []
            current = current_Node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        #Generate Children
        children = current_Node.find_children(maze, end_Node)
        for child in children:
            #Check if child is in closed
            for closed_child in closed_List:
                if child == closed_child:
                    continue
            #Check if child is in open
            for open_node in open_List:
                if child == open_node and child.g_value > open_node.g_value:
                    continue

            open_List.append(child)


sample_maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
answer = Astar_path(sample_maze, (0,0), (7,6))
print(answer)