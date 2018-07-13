"""
Программа для рассчета площади треугольника по местоположению углов.

:Example:

>>> match_S(*get_sides([3, 2], [5, 5], [0, 8]))
10.500000000000002
"""
import doctest
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from numpy import sqrt, mean

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

assert match_c(2, 3) == 3.605551275463989


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

assert get_sides([3, 2], [5, 5], [10, 2]) == \
       (3.605551275463989, 5.830951894845301, 7)


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

assert match_S(*get_sides([3, 2], [5, 5], [10, 2])) == \
       10.500000000000002
assert match_S(*get_sides([3, 2], [5, 5], [10, 2])) == \
       match_S(*get_sides([3, 2], [5, 5], [0, 8]))


def get_points():
    """
    Принимает и проверяет ввод пользователя, возвращает координаты углов.
    Если пользователь дает неверный ввод, пишет в консоль где ошибка.

    :return: координаты углов во вложенных списках вида [[x, y], [x, y], [x, y]].
    :rtype: list of lists
    """
    print('Введите точки углов треугольника в виде координат на осях X и Y.')
    print('На каждый угол введите по 2 координаты через пробел.')

    while True:

        inp1 = input('Угол 1 > ')
        inp2 = input('Угол 2 > ')
        inp3 = input('Угол 3 > ')

        points = []

        for inp in [inp1, inp2, inp3]:

            # проверка на то, что координаты 2
            if len(inp.split()) != 2:
                print('Нужно ввести по 2 координаты на каждый угол (вы ввели {}). '
                      'Попробуйте снова.'.format(len(inp.split())))
                break

            # проверка на числа
            try:
                points.append([float(i) for i in inp.split()])
            except ValueError:
                print('Вы ввели не числа: "{}". Попробуйте снова.'.format(inp))
                break

        else:
            # проверка на то, что координаты не лежат на одной прямой
            if mean([i[0] for i in points]) == points[0][0] or \
                mean([i[1] for i in points]) == points[0][1]:
                print('Введенные точки находятся на одной прямой, попробуйте снова.')
                continue

            return points


class TestMatchC(unittest.TestCase):

    def test_match_c_with_2_and_3_positive(self):
        self.assertEqual(match_c(2, 3), 3.605551275463989,
                         'Wrong hypotenuse len')


    def test_match_c_with_2_and_3_negative(self):
        self.assertIsInstance(match_c(2, 3), float,
                              'Wrong type of hypotenuse len')


class TestGetSides(unittest.TestCase):

    def test_get_sides_with_test_points_positive(self):
        self.assertEqual(get_sides([3, 2], [5, 5], [10, 2]),
                         (3.605551275463989, 5.830951894845301, 7.0),
                         'Wrong sides answer')


    def test_get_sides_returns_strings_positive(self):
        self.assertIsInstance(get_sides([3, 2], [5, 5], [10, 2]), tuple,
                              'Wrong sides type')


class TestMathS(unittest.TestCase):

    def test_match_S_with_abc_positive(self):
        self.assertEqual(match_S(3.605551275463989, 5.830951894845301, 7.0),
                         10.500000000000002, 'Wrong S')


    def test_match_S_int_positive(self):
        self.assertIsInstance(match_S(3.605551275463989, 5.830951894845301, 7.0),
                              float, 'Wrong S type')


class TestGetPoints(unittest.TestCase):

    def test_with_sample_points_positive(self):

        user_input = ['3 2', '5 5', '10 2']  # positive

        expected_points = [[3.0, 2.0], [5.0, 5.0], [10.0, 2.0]]
        expected_stdout = 'Введите точки углов треугольника в виде ' \
                          'координат на осях X и Y.\nНа каждый угол ' \
                          'введите по 2 координаты через пробел.\n'

        stdout_handler = io.StringIO()
        with patch('builtins.input', side_effect=user_input), \
             redirect_stdout(stdout_handler):
            points = get_points()

        got_stdout = stdout_handler.getvalue()

        self.assertEqual(points, expected_points, 'Wrong points')
        self.assertEqual(got_stdout, expected_stdout, 'Wrong stdout')


    def test_without_1_coordinate_negaive(self):

        user_input = [
            '3', '5 5', '10 2',   # negative
            '3 2', '5 5', '10 2'
        ]
        expected_stdout = 'Введите точки углов треугольника в виде ' \
                          'координат на осях X и Y.\nНа каждый угол ' \
                          'введите по 2 координаты через пробел.\nНужно ' \
                          'ввести по 2 координаты на каждый угол ' \
                          '(вы ввели 1). Попробуйте снова.\n'

        stdout_handler = io.StringIO()
        with patch('builtins.input', side_effect=user_input), \
             redirect_stdout(stdout_handler):
            points = get_points()

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(got_stdout, expected_stdout, 'Wrong stdout')


    def test_with_not_number_input_negative(self):

        user_input = [
            'a b', '5 5', '10 2',  # negative
            '3 2', '5 5', '10 2'
        ]
        expected_stdout = 'Введите точки углов треугольника в виде ' \
                          'координат на осях X и Y.\nНа каждый угол ' \
                          'введите по 2 координаты через пробел.\nВы ' \
                          'ввели не числа: "a b". Попробуйте снова.\n'

        stdout_handler = io.StringIO()
        with patch('builtins.input', side_effect=user_input), \
             redirect_stdout(stdout_handler):
            points = get_points()

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(got_stdout, expected_stdout, 'Wrong stdout')


    def test_with_points_on_straight_line_negative(self):

        user_input = [
            '5 4', '5 5', '5 2',   # negative
            '3 2', '5 5', '10 2'
        ]
        expected_stdout = 'Введите точки углов треугольника в виде ' \
                          'координат на осях X и Y.\nНа каждый угол ' \
                          'введите по 2 координаты через пробел.' \
                          '\nВведенные точки находятся на одной прямой, ' \
                          'попробуйте снова.\n'

        stdout_handler = io.StringIO()
        with patch('builtins.input', side_effect=user_input), \
             redirect_stdout(stdout_handler):
            points = get_points()

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(got_stdout, expected_stdout, 'Wrong stdout')


if __name__ == '__main__':

    doctest.testmod()

    unittest.main()

    print('S =', match_S(*get_sides(*get_points())))
