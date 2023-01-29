from project.car import Car


class FamilyCar(Car):

    def drive(self,kilometers):
        fuel_needed = kilometers * FamilyCar.DEFAULT_FUEL_CONSUMPTION
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
