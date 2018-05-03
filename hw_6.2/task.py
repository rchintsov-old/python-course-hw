class Something:​
    def __init__(self, x):​
        self.x = x​

    @prop​
    def attr(self):​
        return self.x ** 2​

    @attr.setter
    def attr_setter(self, update):
        return self.x = update
