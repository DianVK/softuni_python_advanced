from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self,distance):
        needed_fuel = (self.fuel_consumption + Car.CONSUMPTION) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
            return

    def refuel(self,fuel):
        self.fuel_quantity += fuel
        return


class Truck(Vehicle):
    CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self,distance):
        needed_fuel = (self.fuel_consumption + Truck.CONSUMPTION) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
            return

    def refuel(self,fuel):
        self.fuel_quantity += fuel * 0.95
        return


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
