from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def drive(self,kilometers):
        fuel_needed = kilometers * RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
