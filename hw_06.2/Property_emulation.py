class prop:
    """
    Property emulation class.
    """
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if fget and not doc:
            doc = fget.__doc__
        self.__doc__ = doc


    def __get__(self, instance, a):
        if self.fget is None:
            raise AttributeError("can't get the attribute")
        return self.fget(instance)


    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set the attribute")
        return self.fset(instance, value)


    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete the attribute")
        return self.fdel(instance)


    def getter(self, fget):
        self.fget = fget


    def setter(self, fset):
        self.fset = fset


    def deleter(self, fdel):
        self.fdel = fdel


class Something:
    """
    Class for testing.
    """
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        self.x = update


if __name__ == '__main__':

    s = Something(10)
    print(s.attr)

    s.attr = 3
    print(s.attr)
