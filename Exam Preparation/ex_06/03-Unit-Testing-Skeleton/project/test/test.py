from collections import deque

from project.railway_station import RailwayStation
from unittest import TestCase, main

class TestRailwayStation(TestCase):
    name = 'Test Station'
    arrival_trains = []
    departure_trains = []

    def setUp(self):
        self.station = RailwayStation(name="Test Station")

    def test_structure(self):
        self.assertTrue(hasattr(RailwayStation, "new_arrival_on_board"))
        self.assertTrue(hasattr(RailwayStation, "train_has_arrived"))
        self.assertTrue(hasattr(RailwayStation, "train_has_left"))

        self.assertTrue(isinstance(getattr(RailwayStation, "name"), property))

    def test_init(self):
        self.assertEqual('Test Station', self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_setter(self):
        self.station.name = "Test"
        self.assertEqual("Test", self.station.name)
        with self.assertRaises(ValueError) as ex:
            self.station.name = "Te"
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.station.name = "Tes"
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Test Train")
        self.assertEqual(deque(["Test Train"]), self.station.arrival_trains)

    def test_train_has_arrived_other_before(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train 2")
        expect = "There are other trains to arrive before Test Train 3."
        actual = self.station.train_has_arrived('Test Train 3')
        self.assertEqual(expect, actual)

    def test_train_has_arrived_no_initial_trains(self):
        self.station.new_arrival_on_board("Test Train")
        expect = "Test Train is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived('Test Train')
        self.assertEqual(expect, actual)

    def test_train_has_arrived__expect_proper_train_departure(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        expect = "Test Train is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived('Test Train')
        self.assertEqual(expect, actual)

    def test_train_has_arrived__expect_proper_train_arrive_pop(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        self.station.train_has_arrived("Test Train")
        expect = deque(["Test Train2"])
        actual = self.station.arrival_trains
        self.assertEqual(expect, actual)

    def test_train_has_left_empty_station__expect_false(self):
        self.station.new_arrival_on_board("")
        self.station.train_has_arrived("")
        actual = self.station.train_has_left("Test Train")
        self.assertFalse(actual)

    def test_train_has_left__expect_false(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        self.station.train_has_arrived("Test Train")
        self.station.train_has_arrived("Test Train2")

        actual = self.station.train_has_left("Test Train2")
        self.assertFalse(actual)

    def test_train_has_left__expect_true(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.train_has_arrived("Test Train")

        actual = self.station.train_has_left("Test Train")
        self.assertTrue(actual)

if __name__ == '__main__':
    main()
