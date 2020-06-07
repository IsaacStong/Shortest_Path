"""Created by Isaac Stong on 6/6/20
    This file holds the node class for
    Astar search"""
import operator


class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g_value = 0
        self.h_value = 0
        self.f_value = 0

    def __eq__(self, other):
        return self.position == other.position

    #Finds children of self only returns children for squares that are walkable and in dimensions
    def find_children(self, maze, goal):
        children = []
        dimensions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(dimensions)):
            child = Node(self, tuple(map(operator.add, self.position, dimensions[i])))
            if all(j >= 0 for j in child.position) and all(j <= len(maze) for j in child.position):
                if maze[child.position[0]][child.position[1]] == 0:
                    child.find_heuristic(goal)
                    child.g_value = self.g_value + 1
                    child.f_value = child.g_value + child.h_value
                    children.append(child)

        return children

    #Calculates heuristic for a Node
    def find_heuristic(self, goal):
        self.h_value = ((self.position[0] - goal.position[0]) ** 2) + ((self.position[1] - goal.position[1]) ** 2)
