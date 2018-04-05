def fun(string, result = 0):
    '''

    :param str string: строка для конвертации
    :param int result: служебный
    :return: числовое представление строки
    :rtype: int
    '''
    if len(string) > 0:
        # вычисляет на сколько умножать (на сколько сдвинуть)
        current_ord = ord(string[0])
        multiply_index = 0
        while current_ord != 0:
            current_ord = current_ord // 10
            multiply_index += 1
        # обновляет результат
        result = result * (10 ** multiply_index) + ord(string[0])
        # рекурсивный вызов
        return fun(string[1:], result)
    else:
        return result

if __name__ == '__main__':
    fun('abcd')
