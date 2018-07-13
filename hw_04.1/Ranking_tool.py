"""
Tool for ranking students and tasks.
"""
import functools
import itertools

def memoized_once(func):
    """
    Decorator for funcs that need called only once.
    Saves call result to function dict.

    :param function func: function to decorate.
    :return: decorated function.
    :rtype: function
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if func.__dict__.get('result') is None:
            result = func(*args, **kwargs)
            func.__dict__['result'] = result
        return func.__dict__['result']
    return inner


def check_range(low, high):
    """
    Decorator for funcs whose output should match specified boundaries.
    Recalls fuction while the output not matching the boundaries.

    :param (int, float) low: lower bound.
    :param (int, float) high: upper bound.
    :param function func: function to decorate.
    :return: decorated function.
    :rtype: function
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            while True:
                result = func(*args, **kwargs)
                if low <= result <= high:
                    return result
                else:
                    print('Not in range {} - {}. '
                          'Try again.'.format(low, high))
        return inner
    return wrapper


@memoized_once
def get_count_students():
    """Getting count of students"""
    return int(input('Count of students > '))


@memoized_once
def get_count_tasks():
    """Getting count of tasks"""
    return int(input('Count of tasks > '))


@memoized_once
def get_names(st_count):
    """Getting names of students"""
    return [input('Student #{} name > '.format(i + 1))
            for i in range(st_count)]


@check_range(0, 10)
def get_mark(name, task):
    """Getting marks of students for certain student and task"""
    return int(input('Mark for {}, task {} > '.format(name, task)))


@memoized_once
def marks(count_tasks, names):
    """Getting marks of all students by names and count of tasks"""
    return [[(get_mark(name, task + 1), task + 1, name)
             for task in range(count_tasks)] for name in names]


# unites some getting functions
get_marks = lambda: marks(get_count_tasks(),
                          get_names(get_count_students()))


def getting_students_sum(marks):
    """Getting sums of students marks"""
    return [(i, j[0][2]) for i, j in zip([sum([task[0] for task in tasks])
                                          for tasks in marks], marks)]

def getting_tasks_sum(marks):
    """Getting sums of tasks marks"""
    return [(sum([man[i][0] for man in marks]), i+1)
            for i in range(len(marks[0]))]


def who_win(marks):
    """Selects students winners"""
    return [i[1] for i in sorted(getting_students_sum(marks),
                                 key=lambda x: x[0], reverse=True)[:3]]


def task_top(marks):
    """Selects tasks winners"""
    return [i[1] for i in sorted(getting_tasks_sum(marks),
                                 key=lambda x: x[0])[:3]]


def print_winners(result=get_marks()):
    """Printing students winners"""
    print('\nTop-3 students:')
    [print(i) for i in who_win(result)]


def print_task_rank(result=get_marks()):
    """Printing the most difficult tasks"""
    print('\nTop-3 tasks:')
    [print(i) for i in [k for k, g in itertools.groupby(task_top(result))]]


if __name__ == '__main__':
    print_winners()
    print_task_rank()

