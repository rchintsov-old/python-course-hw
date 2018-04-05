
def fabric(fun_2):
    '''
    Декорирует декоратор.
    :param object fun_2: Декоратор, который нужно декорировать
    :return: Декорируемый декоратор
    :rtype: object
    '''
    def deco_main(fun_1):
        def deco_wrapper(f):
            wrapped = fun_2(fun_1(f))
            def fun_wrapper(*args, **kwargs):
               return wrapped(*args, **kwargs)
            return fun_wrapper
        return deco_wrapper
    return deco_main


def lambda_executor(f):
    '''
    Декорирует функцию лямбдой.
    Лямбда размещается внутри этой функции.
    :param object f: декорируемая функция
    :return: функция
    :rtype: object
    '''
    def wrapper():
        # здесь размещается лямбда
        return (lambda x: x**2)(f())
    return wrapper


def repeat(times):
    '''
    Декоратор, вызывает функцию times раз.
    :param int times: сколько раз вызвать декорируемую функцию.
    :return: функцию
    :rtype: object
    '''
    @fabric(lambda_executor)
    def wrapper(f):
        def inner(*args, **kwargs):
            a = [f(*args, **kwargs) for i in range(times)]
            result = sum(a) / len(a)
            return result
        return inner
    return wrapper


@repeat(3)
def foo():
    '''
    Декорируемая функция.
    Принтит собщение 'Foo called!'
    :return: 3
    :rtype: int
    '''
    print('Foo called!')
    return 3



if __name__ == '__main__':
    print(foo())


