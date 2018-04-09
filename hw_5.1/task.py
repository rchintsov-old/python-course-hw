import itertools
import random

class Matrix:
    def __init__(self, *args):
        self._rows = 0
        self._cols = 0
        self._random_bounds = (0, 100)
        self._args = self._check_arguments(args)
        self._matrix = self._create_matrix()
        self._elements = [a for b in self._matrix for a in b]


    def _check_arguments(self, args):

        if len(set([type(i) for i in args])) is not 1:
            print(set([type(i) for i in args]))
            raise ValueError('types is not matching')

        if all(isinstance(n, int) for n in args):
            if len(args) is 2: # это числа
                return args
            else:
                raise ValueError('type 2 arguments for matrix construction')

        if type(args[0]) is list and all(isinstance(n, list) for n in args) and len(args[0]) > 1:
            # print(len(args))
            if sum([len(row) for row in args]) / len(args) != len(args[0]):
                raise ValueError('check the number of lists elements')

            args = args[0]
            return args

        else:
            raise ValueError('incorrect arguments')


    def _create_matrix(self):
        if type(self._args) is tuple:

            self._cols, self._rows = self._args
            return [[random.randint(self._random_bounds[0],
                                    self._random_bounds[1])
                     for i in range(self._cols)]
                    for j in range(self._rows)]

        elif type(self._args) is list:
            self._rows = len(self._args)
            self._cols = len(self._args[0])
            return self._args


    def _flatten(self, list_):
        return [a for b in list_ for a in b]


    def __add__(self, x):
        # проверить на равенство размеров
        if not isinstance(x, Matrix):
            raise TypeError('unsupported operand type for +: {}'.format(type(x)))

        flatten_x = self._flatten(x._matrix)
        if not len(flatten_x) == len(self._elements) \
                and not len(x._matrix) == len(self._matrix):
            raise TypeError("lenght of rows/cols doesn't match")

        res = [i + j for i, j in zip(self._elements, flatten_x)]
        return [list(itertools.islice(res, i, i + self._cols))
                for i in range(0, len(res), self._cols)]


    def __sub__(self, x):
        # проверить на равенство размеров
        if not isinstance(x, Matrix):
            raise TypeError("lenght of rows/cols doesn't match")

        flatten_x = self._flatten(x._matrix)
        if not len(flatten_x) == len(self._elements) \
                and not len(x._matrix) == len(self._matrix):
            raise TypeError("lenght of rows/cols doesn't match")

        res = [i - j for i, j in zip(self._elements, flatten_x)]
        return [list(itertools.islice(res, i, i + self._cols)) for i in range(0, len(res), self._cols)]


    def __mul__(self, x):

        if isinstance(x, (int, float)):
            print(2)
            return [[i * x for i in l] for l in self._matrix]

        elif isinstance(x, Matrix):
            flatten_x = self._flatten(x._matrix)
            if len(flatten_x) == len(self._elements) and len(x._matrix) == len(self._matrix):

                res = [i * j for i, j in zip(self._elements, flatten_x)]

                return [list(itertools.islice(res, i, i + self._cols)) for i in range(0, len(res), self._cols)]

            else:
                raise TypeError("length of rows/cols in matrices doesn't match")

        else:
            print(1)
            raise TypeError('unsupported operand type for *: {}'.format(type(x)))


    def is_equal(self, matrix):
        if not isinstance(matrix, Matrix):
            raise TypeError('unsupported operand type for comparison: {}'.format(type(matrix)))

        if self._matrix == matrix._matrix:
            return True
        else:
            return False


    def is_squared(self):
        if self._rows == self._cols:
            return True
        else:
            return False


    def transpose(self):
        return [[iterable[i] for iterable in self._matrix] for i in range(self._cols)]


    def is_symmetric(self):
        if not self.is_squared():
            raise ValueError('matrix is not squared')

        if self._matrix == self.transpose():
            return True
        else:
            return False


if __name__ == '__main__':

    # генератор рандомной матрицы
    a = Matrix(2, 2)
    print(a._matrix, a._elements, a._cols, a._rows)

    # простая матрица 1
    b = Matrix([[1, 1], [2, 2]])

    # простая матрица 2
    e = Matrix([[3, 3], [4, 4]])

    # арифметические операции с простыми
    print(b + e)
    print(b * e)
    print(e - b)

    # проверка функций
    print(e.transpose(), e.is_symmetric(), e.is_squared())

    # равен ли самому себе
    print(e.is_equal(e))

    # симметричные квадратные матрицы (одинаковые)
    g = Matrix([[1,2,3], [2,1,2], [3,2,1]])
    j = Matrix([[1,2,3], [2,1,2], [3,2,1]])

    # проверка функций
    print(g._matrix, g._elements, g._cols, g._rows, g.is_squared(), g.is_symmetric())

    # равна ли одна другой
    print(g.is_equal(j))

    # сложение неравных по размеру матриц
    print(e + g)

    # неквадратная матрица
    k = Matrix([[1,2,3], [3,2,1]])

    # проверка
    print(k._matrix, k._cols, k._rows, k.transpose(), k.is_squared(), k.is_symmetric())
