from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(30.5, 125.5)

    def test_successful_initialize(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(30.5, self.vehicle.capacity)
        self.assertEqual(125.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_fuel_less_than_needed_raise_exception(self):
        kilometers = 1000
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers)

        self.assertTrue(kilometers * 1.5 > self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_successful_drive(self):
        kilometers = 10
        self.vehicle.drive(kilometers)
        self.assertTrue(kilometers * 1.25 <= self.vehicle.fuel)
        self.assertEqual(18, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_successful_refuel(self):
        self.vehicle.fuel = 10.5
        self.assertTrue(10 + self.vehicle.fuel <= self.vehicle.capacity)
        self.vehicle.refuel(10)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test__str__(self):
        result = self.vehicle.__str__()
        self.assertEqual(f"The vehicle has 125.5 "
               "horse power with 30.5 fuel left"
                " and 1.25 fuel consumption", result)


if __name__ == '__main__':
    main()