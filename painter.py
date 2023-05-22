import matplotlib.pyplot as plt
import numpy as np
from math import *
from Point import Point
from Interval import Interval

STEP_X = 0.001
DOT_COLOR = '#c9007a'
DOT_COLOR_2 = '#000dc9'

def draw(func: str, interval: Interval, points: list[Point]) -> None:
    '''Отрисовка фукнции и точек'''
    # настройка поля для рисования
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)

    # получение интервала и его разбиение с шагом STEP_X
    x_range = list(np.arange(interval.left, interval.right, STEP_X))

    # построение функции и отрисовка
    func_values = function_calculate(func, x_range)

    # отрисовка истинной фукнции и точек
    plt.plot(x_range, func_values, label=func)
    for point in points:
        x = point.x
        y = point.y
        f = eval(func)
        if point.y < f:
            plt.scatter(x, y, color=DOT_COLOR, s=30)
        else:
            plt.scatter(x, y, color=DOT_COLOR_2, s=30)
    plt.legend()
    plt.show()



def function_calculate(func: str, x_values: list[float]) -> list[float]:
    '''Вычисляет для значений x_values значения фукнции func'''
    func_values = []
    for x in x_values:
        func_values.append(eval(func))
    return func_values

