import abc


class Vehicle(metaclass=abc.ABCMeta):
    """
    Abstract class.
    """
    @staticmethod
    def is_motorcycle(wheels):
        if wheels:
            if 1 < wheels <= 3:
                return True
            else:
                return False
        else:
            raise ValueError('vehicle should have a wheels')


    @abc.abstractmethod
    def vehicle_type(self):
        pass

    @abc.abstractmethod
    def purchase_price(self):
        pass

    @abc.abstractmethod
    def vehicle_year(self):
        pass


class Car(Vehicle):
    """Car"""
    def __init__(self, year, model, base_cost):
        super().__init__()
        self.base_cost = base_cost
        self._year = year
        self.model = model

    def purchase_price(self, km):
        return self.base_cost - 0.1 * km

    @property
    def vehicle_type(self):
        return 'car'

    @property
    def vehicle_year(self):
        return self._year


class Motorcycle(Vehicle):
    """Motorcycle"""
    def __init__(self, year, model, base_cost):
        super().__init__()
        self.base_cost = base_cost
        self._year = year
        self.model = model
    
    def purchase_price(self, km):
        return self.base_cost - 0.1 * km
    
    @property
    def vehicle_type(self):
        return 'motorcycle'

    @property
    def vehicle_year(self):
        return self._year


class Truck(Vehicle):
    """Truck"""
    def __init__(self, year, model, base_cost):
        super().__init__()
        self.base_cost = base_cost
        self._year = year
        self.model = model

    def purchase_price(self, km):
        return self.base_cost - 0.1 * km

    @property
    def vehicle_type(self):
        return 'truck'

    @property
    def vehicle_year(self):
        return self._year


class Bus(Vehicle):
    """Bus"""
    def __init__(self, year, model, base_cost):
        super().__init__()
        self.base_cost = base_cost
        self._year = year
        self.model = model

    def purchase_price(self, km):
        return self.base_cost - 0.1 * km

    @property
    def vehicle_type(self):
        return 'bus'

    @property
    def vehicle_year(self):
        return self._year


if __name__ == '__main__':


    bus = Bus(2012, 'Man', 120000)

    print(bus.vehicle_type)
    print(bus.vehicle_year)
    print(bus.model)
    print(bus.purchase_price(10000))
    
    print(
        Vehicle.is_motorcycle(2),
        Vehicle.is_motorcycle(4),
    )




