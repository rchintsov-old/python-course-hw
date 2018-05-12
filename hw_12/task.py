"""
Программа для многопоточной закачки изображений из интернета.
"""
import argparse
import gc
import os
import re
import time
from contextlib import redirect_stdout
from contextlib import suppress
from io import BytesIO
from multiprocessing.pool import ThreadPool

import requests
from PIL import Image
from tqdm import tqdm


class ResolutionError(Exception):
    """
    Inappropriate resolution string.

    :param str message: error explanation.
    :return: raises ResolutionError.
    :rtype: class instance
    """
    def __init__(self, message=''):
       Exception.__init__(self, message)


# поддерживаемые PIL форматы
# http://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html#fully-supported-formats
SUPPORTED_TYPES = {'BMP', 'EPS', 'GIF', 'ICNS', 'ICO', 'IM', 'JPEG', 'JPG',
                   'MSP', 'PCX', 'PNG', 'PPM', 'SGI', 'SPIDER', 'TIFF', 'WebP', 'XBM'}

# настраиваем парсер, заводим аргументы
parser = argparse.ArgumentParser(description='Download and resize images from URL list.')

parser.add_argument('filename', metavar='FILENAME', type=str,
                    help='File with URLs.')

parser.add_argument('--dir', metavar='DIRECTORY', type=str,
                    help='Directory to save the resized files.', default='./')

parser.add_argument('--threads', metavar='N_THREADS', type=int,
                    help='Number of threads for file processing.', default=1)

parser.add_argument('--size', metavar='RESOLUTION', type=str,
                    help='Resolution for image resizing. Should look like "128x128"', default='100x100')

# дополнительно - для tqdm
parser.add_argument('--bar', '-b',
                    help='Shows tqdm progress bar while processing images.',
                    action='store_true')


def check_resolution(resolution):
    """
    Парсит и проверяет переданное разрешение.

    :param str resolution: разрешение.
    :return: преобразованное разрешение изображения.
    :rtype: tuple of ints
    :raises ResolutionError: если resolution не соответствует формату.

    :Example:

    >>> resolution('128x128')
    (128, 128)
    """
    parsed = re.findall('[0-9]+', resolution)
    if len(parsed) == 2:
        return tuple(int(i) for i in parsed)
    else:
        raise ResolutionError('--size parameter should look like "128x128", not {}'
            .format(resolution))


def download_and_resize(params):
    """
    Загружает, изменяет размер и сохраняет файл изображения по его адресу в интернете.

    :param tuple params: (url, filenum, size, dir).
    :param str url: адрес изображения.
    :param str filename: имя файла для сохранения (без расширения).
    :param tuple size: размер изображения в пикселах.
    :param str dir: папка для сохранения файла.
    :return: кортеж, содержащий код завершения функции (0 - норм., 1 - ошибка) и количество байт.
    :rtype: tuple
    """
    url, filenum, size, dir = params

    # пытаемся достать расширение из URL
    try:
        extension = url.split('/')[-1].split('.')[-1]
    except IndexError:
        extension = 'jpg'

    # проверяем на наличие extension в списке поддерживаемых типов
    if extension.upper() not in SUPPORTED_TYPES:
        print('{} wrong filetype: {}'.format(int(filenum), extension.upper()))
        # 1 - код операции (ошибка), 0 - количество байт
        return 1, 0

    filename = filenum + '.' + extension

    # получаем изображение
    r = requests.get(url)
    if r.status_code == 200:

        # попытка чтения в буфер
        try:
            im = Image.open(BytesIO(r.content))
        except OSError:
            print('{} wrong filetype'.format(url))
            return 1, 0

        # ресайз
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(os.path.join(dir, filename))

    # если в запросе код ошибки
    else:
        print('{} URL is not valid: {}'.format(int(filenum), url))
        return 1, 0

    # если всё хорошо
    print('{} saved'.format(int(filenum)))

    # PIL имеет старый баг: объект сохраняется в памяти,
    # когда на него уже вроде бы никто не ссылается,
    # что приводит к переполнению оперативной памяти и свопа.
    # Такое поведение появляется при непонятных условиях, поэтому
    # приходится удалять объект и инициировать сбор мусора вручную.
    # на всякий случай:
    del im
    gc.collect()

    # код операции, количество байт
    return 0, len(r.content)


if __name__ == '__main__':

    # filename, dir, threads, size, verbose
    args = parser.parse_args()

    # создаем папку
    with suppress(FileExistsError):
        os.mkdir(args.dir)

    # попытка прочитать файл с URL
    try:
        with open(args.filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('No such file in directory: {}'.format(args.filename))
        exit(2)

    # чистим строки от лишнего
    URLs = [i.strip('\n') for i in lines if i != '\n']
    # выясняем размер
    size = check_resolution(args.size)

    # префикс для форматирования имен файлов
    prefix = '0{}'.format(len(str(len(URLs))))

    # собираем параметры (аналог product из itertools, но сложнее)
    params = []
    for num, url in enumerate(URLs):
        params.append([url, format(num + 1, prefix), size, args.dir])

    # фиксируем время старта
    start_time = time.time()

    # ------------------- если с progress bar'ом -------------------:
    if args.bar:
        # подавление вывода функции-воркера, чтобы бар нормально отображался:
        with open(os.devnull, 'w') as d:
            with redirect_stdout(d):

                with ThreadPool(args.threads) as pool:

                    # заводим счетчик pbar (для него обязателен close),
                    # вручную указываем количество элементов (total)
                    with tqdm(total=len(URLs)) as pbar:
                        statistics = []

                        # проходимся по итератору imap (вместо map)
                        for stat in pool.imap(download_and_resize, params):
                            statistics.append(stat)
                            # на каждой итерации прибавляем к счетчику 1
                            pbar.update() # == pbar.update(1)

    else:
    # ----------------------------------------------------------------
        with ThreadPool(args.threads) as p:
            statistics = p.map(download_and_resize, params)

    # собираем статистику
    processing_time = time.time() - start_time
    errors_count = sum([i[0] for i in statistics])
    bytes_count = sum([i[1] for i in statistics])

    # выводим в консоль
    print('\nSuccess: {}'.format(len(URLs) - errors_count))
    print('Errors: {}'.format(errors_count))
    print('Bytes received: {}'.format(bytes_count))
    print('Time spent: {} sec'.format(round(processing_time)))
