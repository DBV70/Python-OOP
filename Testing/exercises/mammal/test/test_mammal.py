from project.mammal import Mammal
from unittest import TestCase, main

class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal('TestName', 'TestType', 'TestSound')

    def test_init(self):
        self.assertEqual('TestName', self.mammal.name)
        self.assertEqual('TestType', self.mammal.type)
        self.assertEqual('TestSound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual('TestName makes TestSound', self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual('TestName is of type TestType', self.mammal.info())

if __name__ == '__main__':
    main()
