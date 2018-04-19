import time
from datetime import datetime

class Logger:
    """
    Контекстный менеджер, логгирующий ошибки в файл.
    Не скрывает ошибку, пробрасывает её дальше.
    Если ошибка не произошла, файл не создает и ничего не записывает.
    Время

    Пример вывода в файл:
    Thu Jan  1 03:00:00 1970 | TypeError: something goes wrong | 5.245208740234375e-06

    :param str filename: имя лог-файла, который будет создан.
    :return: лог-файл.
    :rtype: file

    :Example:

    >>> with Logger('log.txt'):
    >>>     print(1)
    # 1

    >>> with Logger('log.txt'):
    >>>    raise TypeError('something goes wrong')
    # TypeError: something goes wrong
    """
    def __init__(self, filename):
        self.start = 0
        self.filename = filename


    def __enter__(self):
        """
        Сохраняет время начала выполнения кода.
        """
        self.start = time.time()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Если ошибка происходит, принимает параметры ошибки.
        Сохраняет их в файл + время ошибки + время выполнения кода.

        :param class exc_type: инстанс ошибки.
        :param str exc_val: детали ошибки.
        :param float self.start: время начала выполнения кода в секундах.
        :return: файл.
        :rtype: file
        """
        if exc_type:
            execution_time = time.time() - self.start
            with open(self.filename, 'a') as f:
                f.write('{time} | {error}: {details} | {execution}\n'.format(
                    time = datetime.fromtimestamp(self.start).strftime("%c"),
                    error = exc_type.__name__,
                    details = exc_val,
                    execution = execution_time
                ))


if __name__ == '__main__':

    with Logger('log.txt'):
        print(1)

    with Logger('log.txt'):
        raise TypeError('something goes wrong')

