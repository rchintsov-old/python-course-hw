import time

class Wine:
    """
    Предоставляет функционал для сохранения и рассчетов параметров вина.

    :param str name: название вина.
    :param str mark: марка вина.
    :param float date: дата розлива (в секундах POSIX time).
    :param str description: Описание.
    :return: объект класса Wine.
    :rtype: object

    :Example:

    >>> wine.details
    # ('Staraya Derevnya', 'Red', 1523225293.021399, 'Zachotnoe')

    >>> wine.set_param('mark', 'White')
    >>> wine.details
    # ('Staraya Derevnya', 'White', 1523225293.021399, 'Zachotnoe')

    >>> wine.how_old
    # 52.395061016082764
    """
    def __init__(self, name, mark, date, description):
        self.name = name
        self.mark = mark
        self.date = date
        self.description = description


    @property
    def details(self):
        """
        Возвращает детали. Может вызываться как метод без скобок.

        :return: кортеж параметров вина.
        :rtype: tuple
        """
        return (self.name, self.mark, self.date, self.description)


    @property
    def how_old(self):
        """
        Возвращает время, прошедшее с даты розлива.

        :return: время, прошедшее с даты розлива (в секундах POSIX time).
        :rtype: float
        """
        return time.time() - self.date


    def set_param(self, param, what):
        """
        Меняет значение параметра по имени.

        :param str param: имя параметра.
        :param what: значение.
        :type what: str or int
        :return: None.
        """
        setattr(self, param, what)


if __name__ == '__main__':

    wine = Wine('Staraya Derevnya', 'Red', time.time(), 'Zachotnoe')
    print(wine.details)
