import time
from datetime import datetime

class Logger:
    def __init__(self, filename):
        self.start = 0
        self.filename = filename

    def __enter__(self):
        self.start = time.time()
        self.file = open(self.filename, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        execution_time = time.time() - self.start
        self.file.write('{time} | {error}: {args} | {execution}'.format(
            time = datetime.fromtimestamp(execution_time).strftime("%c"),
            error = exc_type.__name__,
            args = exc_val,
            execution = execution_time
        ))
        self.file.close()


if __name__ == '__main__':
    with Logger('log.txt'):
        raise TypeError('something goes wrong')

