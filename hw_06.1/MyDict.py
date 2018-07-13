import abc

class MyDict(dict):
    """
    For retrieving and setting arguments by calling a dict object.
    """
    def __call__(self, cls, val=None):
        """
        Get or set a value.

        :param class cls: Currency class child.
        :param (int, float) val: exchange rate.
        :raises ValueError: when got one argument and it is not a class.
        :raises ValueError: when exchange rate < 0.
        """
        if val is None:
            if isinstance(cls, type):
                return self.get(cls.__name__)
            else:
                raise ValueError('the argument should be a class')

        else:
            if isinstance(cls, type) and isinstance(val, (int, float)):
                if val <= 0:
                    raise ValueError('Exchange rate < 0')
                # seting to dict instance
                self[cls.__name__] = val

            else:
                raise ValueError(
                    'The first argument should be a class, '
                    'the second should be > 0.')


class Exchange:
    """
    Descriptor for exchange rate. Method __get__ reloaded.
    """
    def __init__(self, value):
        self.value = MyDict(value)


    def __get__(self, instance, owner):
        return self.value


class Currency(metaclass=abc.ABCMeta):
    """
    Abstract base class for currency.
    """
    def __init__(self, value):
        self.value = value


    @abc.abstractmethod
    def cur(self):
        """
        Currency string representation.
        """
        pass


    def to(self, cls):
        """
        Converts value to other currency.

        :param class cls: other currency class
        :return: instance of specified currency with converted value
        :rtype: Currency class
        """
        if isinstance(self, cls):
            return self
        return cls(self.value * self.course[cls.__name__])


    def __neg__(self, other):
        return self.__class__(-self.value)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.value + other.value)
        else:
            return self + other.to(self.__class__)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            raise ValueError

    def __sub__(self, other):
        return self.__add__(-other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.value > other.value
        else:
            return self > other.to(self.__class__)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return self == other.to(self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value * other)
        else:
            raise ValueError('invalid values for *: {} and {}'.format(
                self.value, other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__mul__(1 / other)

    def __repr__(self):
        return '{:.2f} {}'.format(self.value, self.mark)


class Euro(Currency):
    """
    Euro currency.
    """
    mark = '€'
    course = Exchange({'Dollar': 1.18, 'Rouble': 73.05})

    @property
    def cur(self):
        return 'Евро'


class Dollar(Currency):
    """
    Dollar currency.
    """
    mark = '$'
    course = Exchange({'Euro': 0.85, 'Rouble': 62})

    @property
    def cur(self):
        return 'Доллар'


class Rouble(Currency):
    """
    Rouble currency.
    """
    mark = '₽'
    course = Exchange({'Dollar': 0.016, 'Euro': 0.014})

    @property
    def cur(self):
        return 'Рубль'


if __name__ == '__main__':

    e = Euro(10)
    d = Dollar(20)
    r = Rouble(200)

    print('\n', e, '/', d, '/', r)
    print(e.cur, '/', d.cur, '/', r.cur)

    print('\n{} / $ to €: {}'.format(e, d.to(Euro)))
    print('{} / € to $: {}'.format(e.to(Dollar), d))

    print('\nsum for multiple euro instances:',
        sum([Euro(5) for i in range(5)])
    )

    print('\nsum currencies in rub:', r + d + e)
    print('sum currencies in doll:', d + e + r)

    print('\ncurrencies for euro:', e.course)
    print('euro course for dollar:', e.course(Dollar))
