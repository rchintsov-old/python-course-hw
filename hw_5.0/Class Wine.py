import time

class Wine:
    '''

    >>> wine.details
    # ('Staraya Derevnya', 'Red', 1523225293.021399, 'Zachotnoe')

    >>> wine.set_param('mark', 'White')
    >>> wine.details
    # ('Staraya Derevnya', 'White', 1523225293.021399, 'Zachotnoe')

    wine.how_old
    # 52.395061016082764
    '''

    def __init__(self, name, mark, date, description):
        self.name = name
        self.mark = mark
        self.date = date
        self.description = description


    @property
    def details(self):
        return (self.name, self.mark, self.date, self.description)


    @property
    def how_old(self):
        return time.time() - self.date


    def set_param(self, param, what):
        setattr(self, param, what)


if __name__ == '__main__':
    wine = Wine('Staraya Derevnya', 'Red', time.time(), 'Zachotnoe')
    print(wine.details)
