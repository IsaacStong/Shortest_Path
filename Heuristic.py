"""Created by Isaac Stong on 6/6/20
    Holds heuristic calculation"""
import math


def Heuristic(current, end):
    x1 = current[0]
    x2 = end[0]
    y1 = current[1]
    y2 = end[1]
    dist1 = x2 - x1
    dist2 = y2 - y2
    heuristic = math.sqrt(dist1^2 + dist2^2)
    return heuristic
