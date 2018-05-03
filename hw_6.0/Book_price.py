class Price:
    """
    Дескриптор цены. Ограничивает возможные значения price.
    """
    def __get__(self, instance, owner):
        """
        Возвращает значение price из dict инстанса.

        :param instance instance: инстанс.
        :return: цена.
        :rtype: int
        """
        return instance.__dict__[id(instance)]


    def __set__(self, instance, value):
        """
        Устанавливает значение price в dict инстанса.

        :param instance instance: инстанс.
        :param int value: значение цены.
        :return: None
        :raises ValueError: если значение цены не находится между 0 и 100.
        """
        if not 0 <= value <= 100:
            raise ValueError('Price must be between 0 and 100.')
        instance.__dict__[id(instance)] = value


    def __delete__(self, instance):
        """
        Удаляет значение price из dict инстанса.

        :param instance instance: инстанс.
        :return: None
        """
        instance.__dict__.pop(id(instance))


class Book:
    """
    Класс, хранящий параметры книги.
    Принимает дескриптор класса.

    :Example:

    >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
    >>> b.price
    # 12
    >>> с = Book("William Faulkner", "The Sound and the Fury", 45)
    >>> с.price
    # 45
    >>> b.price = -24
    # ValueError: Price must be between 0 and 100.

    """
    price = Price()

    def __init__(self, author, name, price):
        """
        Инициализирует инстанс класса.

        :param str author: автор книги.
        :param str name: имя автора.
        :param int price: цена книги.
        :return: инстанс класса.
        :rtype: instance
        :raises ValueError: наследуется от дескриптора Price
        """
        self.author = author
        self.name = name
        self.price = price


if __name__ == '__main__':

    b = Book("William Faulkner", "The Sound and the Fury", 12)
    c = Book("William Faulkner", "The Sound and the Fury", 45)

    print(b.price)
    print(c.price)

    b.price = -24
