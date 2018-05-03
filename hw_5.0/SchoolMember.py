class SchoolMember:
    """
    Родительский класс.

    :param str name: имя.
    :param int age: возраст.
    :return: объект "SchoolMember"
    :rtype: object
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создан SchoolMember: {}'.format(name))


class Teacher(SchoolMember):
    """
    Класс "учитель" Наследует значения от класса SchoolMember.

    :param str name: имя.
    :param int age: возраст.
    :param int paid: зарплата.
    :return: объект "Teacher".
    :rtype: object
    """
    def __init__(self, name, age, paid):
        super().__init__(name=name, age=age)
        self.paid = paid
        print('Создан Teacher: {}'.format(self.name))


    def show(self):
        """
        Принтит параметры класса.

        :return: параметры класса.
        :rtype: консольный вывод
        """
        print('Имя: "{}" Возраст: "{}" Зарплата: "{}"'.format(self.name, self.age, self.paid))


class Student(SchoolMember):
    """
    Класс "студент" Наследует значения от класса SchoolMember.

    :param str name: имя.
    :param int age: возраст.
    :param int marks: оценки.
    :return: объект "Student".
    :rtype: object
    """
    def __init__(self, name, age, marks):
        super().__init__(name=name, age=age)
        self.marks = marks
        print('Создан Student: {}'.format(self.name))


    def show(self):
        """
        Принтит параметры класса.

        :return: параметры класса.
        :rtype: консольный вывод
        """
        print('Имя: "{}" Возраст: "{}" Оценки: "{}"'.format(self.name, self.age, self.marks))


if __name__ == '__main__':

    persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]
    for person in persons:
        person.show()

