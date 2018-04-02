# Заводит переменную справочника
catalog = {}

def checked_input(values, type_, hello):
    '''Проверяет ввод на принадлежность множеству правильных вариантов'''
    inp = type_(input(hello))
    if inp not in values:
        while inp not in values:
            print('Incorrect input, try again')
            inp = type_(input(hello))
    return inp


def add_number(name, number):
    '''Добавляет имя в справочник'''
    global catalog
    if name not in catalog:
        catalog[name] = []
    catalog[name].append(number)


def add_number_and_name():
    '''Запрашивает у пользователя имя и номер для добавления в справочник.
    Вызывает функцию добавления.
    '''
    name = input('Type a name >')
    number = int(input('Type a number >'))
    add_number(name=name, number=number)


def get_numbers():
    '''Запрашивает у пользователя имя и показывает номера из справочника по нему.
    Если имени нет в правочнике, сообщает об этом.
    '''
    name = input('Type a name >')
    if name in catalog:
        numbers = catalog[name]
        print('name', '\t', 'number')
        for num in numbers:
            print(name, '\t', num)
    else:
        print('{} not in catalog'.format(name))


def del_numbers():
    '''Запрашивает у пользователя имя и удаляет запись о нем из справочника.
    Если имени нет в правочнике, сообщает об этом.'''
    global catalog
    name = input('Type a name >')
    if name in catalog:
        catalog.pop(name)
        print(name, 'deleted')
    else:
        print('{} not in catalog'.format(name))


def main():
    '''Запускает программу'''
    print('''
    Hello!
    What are you want to do?
    1 - add name and number
    2 - show numbers by name
    3 - delete numbers by name
    ''')

    inp = checked_input([1,2,3], int, 'Type a digit >')

    if inp == 1:
        add_number_and_name()
    elif inp == 2:
        get_numbers()
    elif inp == 3:
        del_numbers()
