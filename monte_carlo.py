import numpy as np
from math import *
from Interval import Interval
from Point import Point
import random
def monte_carlo(func: str, interval: Interval, count_points: int, step: float) -> tuple[float, list[Point]]:
    x = interval.left 
    min_func_value = 0.0 
    max_func_value = eval(func) 

    # нахождение локальных минимума и максимума
    for x in np.arange(interval.left, interval.right, step):
        if eval(func) > max_func_value:
            max_func_value = eval(func)
        if eval(func) < min_func_value:
            min_func_value = eval(func)

    # генерация случайных точек x = [a, b),
    # f(x) = [min_func_value, max_func_value)
    points_below = [] # точки ниже кривой
    points_heigher = [] # точки выше кривой
    for _ in range(count_points):
        x = random.uniform(interval.left, interval.right)
        y = random.uniform(min_func_value, max_func_value)

        if y < eval(func):
            points_below.append(Point(x=x, y=y))
        else:
            points_heigher.append(Point(x=x, y=y))

    area = (max_func_value-min_func_value)*(interval.right - interval.left) # площадь прямоугольника

    # замена знака, если график лежит ниже оси ОX
    sign = 1
    if min_func_value < 0:
        sign = -1

    result = sign*area*len(points_below)/count_points
    points = points_below + points_heigher
    return (result, points)
