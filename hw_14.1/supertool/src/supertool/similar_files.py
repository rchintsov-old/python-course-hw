import sys
import hashlib
import os
import doctest

BUFFER_SIZE = 20971520  # 20 Mb per iteration
INITIAL_DIR = os.getcwd()


def md5_calc(filename):
    """
    Функция для расчета MD5 хеш суммы.

    :param str filename: имя файла.
    :return: MD5 hash string.
    :rtype: str

    :Example:

    >>> md5_calc('../tests/duplicates/non_dupl.txt')
    'aa6c1acf485ea24d50f0c55dc0e7944a'
    """
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()


def get_filelist(target_dir):
    """
    Получает список файлов из целевой директории.

    :param str target_dir: целевая директория поиска.
    :return: список файлов (директории игнорирует).
    :rtype: list

    :Example:

    >>> get_filelist('../tests/duplicates')
    ['dupl_2.txt', 'non_dupl.txt', 'dupl_1.txt']
    """
    os.chdir(target_dir)
    filelist = [i for i in os.listdir() if os.path.isfile(i)]

    return filelist


def compare_md5_sums(filelist):
    """
    Сравнивает контрольные суммы списка переданных файлов и отдает
    словарь дубликатов (ключи - MD5).

    :param list filelist: список файлов для расчета MD5.
    :return: словарь с дублирующимися файлами.
    :rtype: dict

    :Example:

    >>> compare_md5_sums(['../setup.py'])
    {}
    >>> compare_md5_sums(['similar_files.py', 'similar_files.py']).values()
    dict_values([['similar_files.py', 'similar_files.py']])
    """
    hash_db = []
    for file in filelist:
        hash_db.append((md5_calc(file), file))

    md5_collection = [i[0] for i in hash_db]
    similar_files = {}

    for hash_ in md5_collection:
        if md5_collection.count(hash_) > 1:
            similar_files.update({
                hash_: [i[1] for i in hash_db if i[0] == hash_]
            })

    return similar_files


def print_similar(similar_files, target_dir):
    """
    Выводит дубликаты в консоль, если они есть.
    В ином случае сообщает, что их нет.

    :param dict similar_files: словарь с одинаковыми файлами.
    :param str target_dir: директория, в которой производился поиск.
    :return: консольный вывод.

    :Example:

    >>> print_similar({}, '/home')
    <BLANKLINE>
    Search path: /home
    No similar files.
    >>> print_similar({'123': ['a.txt', 'b.txt']}, '/')
    <BLANKLINE>
    Search path: /
    <BLANKLINE>
    1 group(s) of similar files found:
    group 1: a.txt, b.txt
    """
    print('\nSearch path: {}'.format(target_dir))

    if similar_files:
        print('\n{count} group(s) of similar files found:'.format(
            count = len(similar_files),
        ))

        for num, group in enumerate(similar_files):
            print('group {}:'.format(num + 1), end=' ')
            print(', '.join(similar_files[group]))

    else:
        print('No similar files.')


def main(target_dir=os.getcwd()):
    """
    Запуск программы.

    :param str target_dir: целевая директория (по умолчанию - текущая).
    :return: список файлов-дубликатов.
    :rtype: console output

    :Example:

    >>> main('./')
    <BLANKLINE>
    Search path: ./
    No similar files.
    >>> main('../tests/duplicates')
    <BLANKLINE>
    Search path: ../tests/duplicates
    <BLANKLINE>
    1 group(s) of similar files found:
    group 1: dupl_2.txt, dupl_1.txt
    """
    filelist = get_filelist(target_dir)

    similar_files = compare_md5_sums(filelist)

    print_similar(similar_files, target_dir)
    # возвращает интерпретатор в начальную директорию
    os.chdir(INITIAL_DIR)


if __name__ == '__main__':

    doctest.testmod()

    main()
