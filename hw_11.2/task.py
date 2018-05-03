"""
Программа для рассчета площади треугольника по местоположению углов.

:Example:

>>> match_S(*get_sides([3, 2], [5, 5], [0, 8]))
10.500000000000002
"""
from numpy import sqrt, mean


class InputError(Exception):
    """
    Inappropriate input.

    :param str message: error explanation (optional).
    :return: InputError.
    :rtype: class instance
    """
    def __init__(self, message=''):
       Exception.__init__(self, message)



# --------------------------------------------------
point1 = [3,2]
point2 = [5,5]
point3 = [10,2]

a, b, c = 3.605551275463989, 5.830951894845301, 7
S = 10.500000000000002
# --------------------------------------------------


def match_c(a, b):
    """
    Вычисляет гипотенузу треугольника.

    :param (int, float) a: сторона A.
    :param (int, float) b: сторона B.
    :return: сторона C.
    :rtype: int, float

    :Example:

    >>> match_c(2, 3)
    3.605551275463989
    """
    return sqrt(a ** 2 + b ** 2)

assert match_c(2, 3) == a


def get_sides(point1, point2, point3):

    """
    Вычисляет длины сторон треугольника по координатам углов вида [x, y].

    :param list point1: координаты угла 1.
    :param list point2: координаты угла 2.
    :param list point3: координаты угла 3.
    :return: длины сторон треугольника.
    :rtype: tuple

    :Example:

    >>> get_sides([3, 2], [5, 5], [10, 2])
    (3.605551275463989, 5.830951894845301, 7.0)
    """
    # 1. попарное вычитание одной координаты из лругой по каждой из осей
    # 2. получение сторон для "служебного" треугольника, у которого гипотенуза
    # является длиной стороны исходного треугольника, которую мы ищем
    # 3. вычисление неизвестной гипотенузы = длины стороны начального треугольника
    a = match_c(*[max([k, l]) - min([k, l]) for k, l in zip(point1, point2)])
    b = match_c(*[max([k, l]) - min([k, l]) for k, l in zip(point2, point3)])
    c = match_c(*[max([k, l]) - min([k, l]) for k, l in zip(point1, point3)])

    return a, b, c

assert get_sides(point1, point2, point3) == (a, b, c)


def match_S(a, b, c):
    """
    Вычисляет площадь треугольника по длинам его сторон.

    :param float a: длина стороны A.
    :param float b: длина стороны B.
    :param float c: длина стороны C.
    :return: площадь треугольника.
    :rtype: float

    :Example:

    >>> match_S(3.605551275463989, 5.830951894845301, 7.0)
    10.500000000000002
    """
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

assert match_S(*get_sides(point1, point2, point3)) == S
assert match_S(*get_sides(point1, point2, point3)) == \
       match_S(*get_sides(point1, point2, [0, 8]))


def fake_input(str_):
    """
    For testing input with doctest.

    :param str str_: строка для вывода в консоль.
    :return: 1.
    :rtype: int

    :Example:

    >>> fake_input('some string')
    1
    """
    return 1


def get_input(input_func=input):
    """
    Принимает ввод пользователя.

    :return: координаты углов [point_1, point_2, point_3].
    :rtype: list of strings

    :Example:

    >>> get_input(fake_input)
    (1, 1, 1)
    """
    inp1 = input_func('Угол 1 > ')
    inp2 = input_func('Угол 2 > ')
    inp3 = input_func('Угол 3 > ')
    return inp1, inp2, inp3



def get_points(inp1='', inp2='', inp3='', test=False):
    """
    Принимает и проверяет ввод пользователя, возвращает координаты углов.
    Если пользователь дает неверный ввод, пишет в консоль где ошибка.

    :return: координаты углов во вложенных списках вида [[x, y], [x, y], [x, y]].
    :rtype: list
    :exception ValueError: когда пользователь вводит не числа (перехватывается).

    :Example:

    >>> get_points('3 2', '5 5', '10 2', test=True)
    Введите точки углов треугольника в виде координат на осях X и Y.
    На каждый угол введите по 2 координаты через пробел.
    [[3.0, 2.0], [5.0, 5.0], [10.0, 2.0]]
    >>> get_points('3', '5 5', '10 2', test=True)
    Traceback (most recent call last):
    ...
    InputError: 2 coordinates needed
    >>> get_points('a b', '5 5', '10 2', test=True)
    Traceback (most recent call last):
    ...
    InputError: not numbers
    >>> get_points('5 4', '5 5', '5 2', test=True)
    Traceback (most recent call last):
    ...
    InputError: all points are on the straight line
    """
    print('Введите точки углов треугольника в виде координат на осях X и Y.')
    print('На каждый угол введите по 2 координаты через пробел.')

    while True:

        if not test:
            inp1, inp2, inp3 = get_input()

        points = []

        for inp in [inp1, inp2, inp3]:

            # проверка на то, что координаты 2
            if len(inp.split()) != 2:
                print('Нужно ввести по 2 координаты на каждый угол (вы ввели {}). '
                      'Попробуйте снова.'.format(len(inp.split())))

                if not test:
                    break
                else:
                    raise InputError("2 coordinates needed")

            # проверка на числа
            try:
                points.append([float(i) for i in inp.split()])
            except ValueError:
                print('Вы ввели не числа: "{}". Попробуйте снова.'.format(inp))

                if not test:
                    break
                else:
                    raise InputError("not numbers")

        else:
            # проверка на то, что координаты не лежат на одной прямой
            if mean([i[0] for i in points]) == points[0][0] or \
                mean([i[1] for i in points]) == points[0][1]:
                print('Введенные точки находятся на одной прямой, попробуйте снова.')
                if not test:
                    continue
                else:
                    raise InputError('all points are on the straight line')

            return points



if __name__ == '__main__':

    import doctest
    doctest.testmod()

    # print('S =', match_S(*get_sides(*get_points())))
