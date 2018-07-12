import time
import functools


def trace(func):
    '''
    Декоратор, который выполняет декорируемую функцию и выводит время её работы.
    :param object func: функция для декорирования
    :return: результат работы декорируемой функции
    :rtype: object
    '''
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start_time)
        return result
    return inner


@trace
def sleep(sec):
    '''
    Ждет sec секунд и возвращает 'Hello'
    :param int sec: время ожидания в секундах
    :return: Hello
    :rtype: str
    '''
    time.sleep(sec)
    return 'Hello'


if __name__ == '__main__':
    print(sleep(2))
