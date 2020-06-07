"""Created by Isaac Stong on 6/6/20
    This file holds the node class for
    Astar search"""
import operator
import math


class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g_value = 0
        self.h_value = 0
        self.f_value = 0

    def __eq__(self, other):
        return self.position == other.position

    def find_children(self, maze, goal):
        children = []
        dimensions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(dimensions)):
            child = Node(self, tuple(map(operator.add, self.position, dimensions[i])))
            if all(j >= 0 for j in child.position) and all(j <= len(maze) for j in child.position):
                if maze[child.position[0]][child.position[1]] == 0:
                    child.find_heuristic(goal.position)
                    child.g_value = self.g_value + 1
                    child.f_value = child.g_value + child.h_value
                    children.append(child)

        return children

    #Calculates heuristic for a Node
    def find_heuristic(self, goal):
        x1 = self.position[0]
        x2 = goal[0]
        y1 = self.position[1]
        y2 = goal[1]
        dist1 = x2 - x1
        dist2 = y2 - y1
        heuristic = math.sqrt(dist1 ** 2 + dist2 ** 2)
        self.h_value = heuristic
