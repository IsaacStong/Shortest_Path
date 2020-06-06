"""Created by Isaac Stong on 6/6/20
    This file holds the node class for
    Astar search"""


class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g_value = 0
        self.h_value = 0
        self.f_value = 0

    def __eq__(self, other):
        return self.position == other.position

