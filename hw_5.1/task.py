import itertools

class Matrix:
    def __init__(self, *args):
        self._args = self._check_values(args)
        self._matrix = self._create_matrix()
        self._rows = 0
        self._cols = 0
        self._elements = [a for b in self._matrix for a in b]


    def _check_values(self, args):
        # print(args)
        # _args = _args[0]
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

            x, y = self._args
            self._matrix = [[random.randint(0, 100) for i in range(x)] for i in range(y)]
            self._cols = x
            self._rows = y

        elif type(self._args) is list:
            self._rows = len(args)
            self._cols = len(args[0])
            return self._args


    def _flatten(self, list_):
        return [a for b in list_ for a in b]


    def __add__(self, x):
        # проверить на равенство размеров
        if type(x) is Matrix:
            flatten_x = self._flatten(x)
            if len(flatten_x) == len(self._elements) and len(x) == len(self._matrix):

                res = [i + j for i, j in zip(self._elements, flatten_x)]

                return [list(itertools.islice(res, i, i + self._cols)) for i in range(0, len(res), self._cols)]

            else:
                raise TypeError("lenght of rows/cols doesn't match")
        else:
            raise TypeError('unsupported operand type for +: {}'.format(type(x)))


    def __sub__(self, x):
        # проверить на равенство размеров
        if type(x) is Matrix:
            flatten_x = self._flatten(x)
            if len(flatten_x) == len(self._elements) and len(x) == len(self._matrix):

                res = [i - j for i, j in zip(self._elements, flatten_x)]
                return [list(itertools.islice(res, i, i + self._cols)) for i in range(0, len(res), self._cols)]

            else:
                raise TypeError("lenght of rows/cols doesn't match")
        else:
            raise TypeError('unsupported operand type for +: {}'.format(type(x)))


    def __mul__(self, x):
        if type(x) is int or float:
            return [[i * x for i in l] for l in self._matrix]

        elif type(x) is Matrix:
            flatten_x = self._flatten(x)
            if len(flatten_x) == len(self._elements) and len(x) == len(self._matrix):

                res = [i * j for i, j in zip(self._elements, flatten_x)]

                return [list(itertools.islice(res, i, i + self._cols)) for i in range(0, len(res), self._cols)]

            else:
                raise TypeError("lenght of rows/cols doesn't match")
        else:
            raise TypeError('unsupported operand type for *: {}'.format(type(x)))






#
# a = Matrix([[1, 1], [2,2]])
# b = Matrix(1, 1)
# # c = Matrix([[1, 1], [2,2]])
# a._args
# a._cols
# b._args
# d._cols
# # c._args
# #
# # a.__getattribute__
# #
# # a.__multiply__
