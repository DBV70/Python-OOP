from project.furniture import Furniture
from unittest import TestCase, main

class FurnitureTests(TestCase):
    def setUp(self):
        self.furniture = Furniture('TestModel',  25.5, (10, 20, 30))

    def test_init(self):
        self.assertEqual('TestModel', self.furniture.model)
        self.assertEqual(25.5, self.furniture.price)
        self.assertEqual((10, 20, 30), self.furniture.dimensions)
        self.assertEqual(True, self.furniture.in_stock)
        self.assertEqual(None, self.furniture.weight)

    def test_model_setter(self):
        self.furniture.model = 'NewModel'
        self.assertEqual('NewModel', self.furniture.model)
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = ''
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = 'a' * 51
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_price_setter(self):
        self.furniture.price = 10.5
        self.assertEqual(10.5, self.furniture.price)
        with self.assertRaises(ValueError) as ex:
            self.furniture.price = -10
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_dimensions_setter(self):
        self.furniture.dimensions = (10, 20, 30)
        self.assertEqual((10, 20, 30), self.furniture.dimensions)
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (10, 20)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (10, 20, 30, 40)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (10, 20, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_weight_setter(self):
        self.furniture.weight = 10
        self.assertEqual(10, self.furniture.weight)
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = -10
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_get_available_status(self):
        self.assertEqual("Model: TestModel is currently in stock.", self.furniture.get_available_status())
        self.furniture.in_stock = False
        self.assertEqual("Model: TestModel is currently unavailable.", self.furniture.get_available_status())

    def test_get_specifications(self):
        self.assertEqual("Model: TestModel has the following dimensions: 10mm x 20mm x 30mm and weighs: N/A", self.furniture.get_specifications())
        self.furniture.weight = 10
        self.assertEqual("Model: TestModel has the following dimensions: 10mm x 20mm x 30mm and weighs: 10", self.furniture.get_specifications())

if __name__ == '__main__':
    main()
