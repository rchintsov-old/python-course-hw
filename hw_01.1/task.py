# # Задание 1.1 - Оценки
# Вам необходимо написать программу на языке Python, которая выполняет следующий алгоритм.
#
# 1. Спрашивает количество студентов на курсе
stud_count = int(input('Count of students >'))

# 2. Спрашивает количество заданий на курсе
tasks_count = int(input('Count of tasks >'))

# 3. Запрашивает имена каждого из студентов
students = []
for n in range(stud_count):
    students.append(input('Student #{} name >'.format(n + 1)))

# 4. Запрашивает оценку по шкале от 0 до 10 (только целые числа) для каждого студента и каждого задания
all_marks = []
students_rank = {}
for student in students:
    print('Student {}:'.format(student))
    marks_raw = []
    for n_task in range(tasks_count):
        mark = int(input('Type a mark for task #{} (from 0 to 10)'.format(n_task + 1)))
        marks_raw.append(mark)
        all_marks.append({'n_task': n_task, 'mark': mark})

    marks_sum = 0
    for i in marks_raw:
        marks_sum += i
    marks_mean = marks_sum / tasks_count

    students_rank.update({marks_mean: student})

tasks_rank = {}
for n_task in range(tasks_count):
    task_marks = []
    for mark in all_marks:
        if mark['n_task'] == n_task:
            task_marks.append(mark['mark'])

    marks_sum = 0
    for i in task_marks:
        marks_sum += i
    task_marks_mean = marks_sum / len(task_marks)

    tasks_rank.update({task_marks_mean: n_task})


# 5. Выводит ТОП-3 студента по рейтингу и ТОП-3 самых сложных заданий (тех, в которых студенты в сумме набрали меньше всего баллов)
mm = list(students_rank)
mm.sort(reverse=True)
tm = list(tasks_rank)
tm.sort()

print('Top-3 students:')
for j, i in enumerate(mm[:3]):
    print(j + 1, students_rank[i])

print('Top-3 tasks:')
for j, i in enumerate(tm[:3]):
    print(j + 1, tasks_rank[i] + 1)




# ## Дополнительно
# 1. Ввод и вывод производится через функции input и print
# 2. Для прохода цикла N раз по операциям рекоммендуется использовать конструкцию `for i in range(students_count):`
# 3. Программа должна быть представлена в виде одного файла с именем task.py
#
# ## Deadline
# **30.03.2018**

