from project.vehicle import Vehicle
from unittest import TestCase, main

class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 100)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_raises_if_not_enough_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        self.vehicle.fuel = 125
        self.vehicle.drive(100)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_raises_if_not_enough_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(150)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(50)
        self.assertEqual(100, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption", str(self.vehicle))

if __name__ == '__main__':
    main()
