from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self,kilometers):
        fuel_needed = kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed

