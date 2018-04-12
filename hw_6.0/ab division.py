class Error_code(Exception):
   def __init__(self, what):
       Exception.__init__(self, what)


def main():
    """
    Ожидает ввод от пользователя:
    1) количество пар
    2) пары по количеству
    Делит одно число на другое.

    :return: вывод от деления.
    :rtype: console output
    :exception ValueError: когда вместо числа пар введено не число (int).
    :exception ZeroDivisionError: при попытке деления на 0.
    :exception ValueError: при попытке деления не на число.
    :raises Error_code: если деление невозможно.
    """
    cnt = ''
    # проверяет ввод
    while not isinstance(cnt, int):
        cnt = input('Введите число пар >')
        try:
            cnt = int(cnt)
        except ValueError:
            pass

    # создает объект из которого потом берет аргументы для деления
    to_div = []
    for i in range(cnt):
        to_div.append(tuple(i for i in input('Введите пару через пробел>').split(' ')))

    # деление и перехват ошибок
    for i, j in to_div:
        try:
            try:
                a = int(i) / int(j)
            # else: - закомменчено из-за пайчарма, он не знает, что так можно
                print(a)
            # перехват стандартных ошибок, вызов кастомной ошибки
            except (ZeroDivisionError, ValueError) as e:
                raise Error_code(e.args[0])
        # кастомный консольный вывод
        except Error_code as ec:
            print('Error code:', ec)
            continue


if __name__ == '__main__':
    main()
