import abc


class Vehicle(metaclass=abc.ABCMeta):
    """
    Abstract class.
    """
    def __init__(self):
        self.base_cost = None

    @abc.abstractmethod
    def vehicle_type(self):
        pass

    @staticmethod
    def is_motorcycle(self, wheels):
        if wheels:
            if 1 < wheels <= 3:
                return True
            else:
                return False
        else:
            raise ValueError('vehicle should have a wheels')

    @classmethod
    def purchase_price(self, base_cost, km):
        if self.base_cost != None:
            return self.base_cost - 0.1 * km
        else:
            return base_cost - 0.1 * km

    @abc.abstractmethod
    def vehicle_year(self):
        pass

    @abc.abstractmethod
    def model(self):
        pass


class Car(Vehicle):
    def __init__(self, year, model, base_cost, passed_km):
        super().__init__()
        self.base_cost = base_cost
        self.passed_km = passed_km
        self.year = year
        self.model_ = model

    @property
    def vehicle_type(self):
        return 'car'

    @property
    def vehicle_year(self):
        return self.year

    @property
    def model(self):
        return self.model_


class Motorcycle(Vehicle):
    def __init__(self, year, model, base_cost, passed_km):
        super().__init__()
        self.base_cost = base_cost
        self.passed_km = passed_km
        self.year = year
        self.model_ = model

    @property
    def vehicle_type(self):
        return 'motorcycle'

    @property
    def vehicle_year(self):
        return self.year

    @property
    def model(self):
        return self.model_


class Truck(Vehicle):
    def __init__(self, year, model, base_cost, passed_km):
        super().__init__()
        self.base_cost = base_cost
        self.passed_km = passed_km
        self.year = year
        self.model_ = model

    @property
    def vehicle_type(self):
        return 'truck'

    @property
    def vehicle_year(self):
        return self.year

    @property
    def model(self):
        return self.model_


class Bus(Vehicle):
    def __init__(self, year, model, base_cost, passed_km):
        super().__init__()
        self.base_cost = base_cost
        self.passed_km = passed_km
        self.year = year
        self.model_ = model

    @property
    def vehicle_type(self):
        return 'bus'

    @property
    def vehicle_year(self):
        return self.year

    @property
    def model(self):
        return self.model_


if __name__ == '__main__':

    bus = Bus(2012, 'Man', 120000, 10000)
    bus.vehicle_type



