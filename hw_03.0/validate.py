import functools

def validate(low_bound, upper_bound):
    """
    Проверяет попадание параметров декорируемой функции в допустимый диапазон
    и выполняет её в случае прохождения проверки.
    :param int low_bound: нижняя граница
    :param int upper_bound: верхняя граница
    :return: декорируемую функцию
    :rtype: object
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(tpl):
            func.do = True
            for i in tpl:
                if not low_bound <= i <= upper_bound:
                    func.do = False
            if func.do:
                return func(tpl)
        return inner
    return wrapper


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    """
    Создает пиксель в заданном диапазоне.
    Выводит сообщение об успехе в случае выполнения.
    :param iterable pixel_values:
    :return: сообщение 'Pixel created!'
    :rtype: None
    """
    print('Pixel created!')


if __name__ == '__main__':
    set_pixel([0, 1, 2])
