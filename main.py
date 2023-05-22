import numpy as np
from math import *

from Interval import Interval
from simpson import *
from monte_carlo import *
from painter import draw


def main():
    func = str(input('Функция>'))

    left = float(input('Нижняя граница интегрирования>'))
    right = float(input('Верхняя граница интегрирования>'))
    interval = Interval(left=left, right=right)

    amount_points = float(input('Шаг>'))
    #start_step = (right-left)/amount_points
    start_step = amount_points

    count_points = int(input('Количество точек>'))

    print(f'∫{func} от {interval.left} до {interval.right} равен:')

    smp = simpson(func=func, interval=interval, step=start_step)
    # метод Симпсона
    print(f'метод Симпсона: {smp}')

    # метод Монте-Карло
    mc = monte_carlo(func=func, interval=interval, \
                     count_points=count_points, step=start_step)
    print(f'метод Монте-Карло: {mc[0]}')

    delta = abs(mc[0] - smp)
    print(f'Дельта: {delta}')

    draw(func=func, interval=interval, points=mc[1])


if __name__ == '__main__':
    main()
