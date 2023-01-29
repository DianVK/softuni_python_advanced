from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self,kilometers):
        fuel_needed = kilometers * SportCar.DEFAULT_FUEL_CONSUMPTION
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
