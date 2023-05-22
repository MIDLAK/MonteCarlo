import numpy as np
from math import *

from Interval import Interval
from simpson import *
from monte_carlo import *


def main():
    func = str(input('Функция>'))

    left = float(input('Нижняя граница интегрирования>'))
    right = float(input('Верхняя граница интегрирования>'))
    interval = Interval(left=left, right=right)

    amount_points = int(input('Количество отрезков>'))
    #start_step = (right-left)/amount_points
    start_step = 1/amount_points

    print(f'∫{func} от {interval.left} до {interval.right} равен:')

    # метод Симпсона
    print(f'метод Симпсона: {simpson(func=func, interval=interval, step=start_step)}')

    # метод Монте-Карло
    print(monte_carlo(func=func, interval=interval, count_points=10000, step=start_step)[0])


if __name__ == '__main__':
    main()
