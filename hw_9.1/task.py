import time
from datetime import datetime

class Logger:
    """
    Контекстный менеджер, логгирующий ошибки в файл.
    Не скрывает ошибку, пробрасывает её дальше.
    Если ошибка не произошла, файл не создает и ничего не записывает.

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
        self.start = time.time()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Если ошибка происходит, принимает параметры ошибки.
        Сохраняет их в файл + время ошибки + время выполнения кода.
        
        :param class exc_type: класс ошибки.
        :param Error exc_val: детали ошибки.
        :return: файл.
        :rtype: file
        """

        if exc_type:
            execution_time = time.time() - self.start
            with open(self.filename, 'a') as f:
                f.write('{time} | {error}: {args} | {execution}'.format(
                    time = datetime.fromtimestamp(execution_time).strftime("%c"),
                    error = exc_type.__name__,
                    args = exc_val,
                    execution = execution_time
                ))


if __name__ == '__main__':

    with Logger('log.txt'):
        print(1)

    with Logger('log.txt'):
        raise TypeError('something goes wrong')

