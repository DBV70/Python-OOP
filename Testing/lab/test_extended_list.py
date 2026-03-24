class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase, main

class ListTest(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(100, 1, 20)

    def test_init(self):
        l = IntegerList(1, "2", 10.7, 6)
        self.assertEqual(l.get_data(), [1, 6])

    def test_add_not_int_raises(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

        with self.assertRaises(ValueError) as ex:
            self.integer_list.add([])
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

    def test_add(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        result = self.integer_list.add(100)
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20, 100])
        self.assertEqual(result, [100, 1, 20, 100])

    def test_remove_index_out_of_range_raises(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

    def test_remove_index(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        result = self.integer_list.remove_index(1)
        self.assertEqual(self.integer_list.get_data(), [100, 20])
        self.assertEqual(result, 1)

    def test_get_invalid_index_raises(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

    def test_get(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        result = self.integer_list.get(0)
        self.assertEqual(result, 100)

    def test_insert_invalid_index_raises(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(100, 5)
        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

    def test_insert_invalid_element_raises(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, "5")
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])

    def test_insert(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        result = self.integer_list.insert(1, 5)
        self.assertEqual(self.integer_list.get_data(), [100, 5, 1, 20])
        self.assertIsNone(result)

    def test_get_biggest(self):
        self.integer_list.insert(0, 30)
        self.assertEqual(self.integer_list.get_data(), [30, 100, 1, 20])
        result = self.integer_list.get_biggest()
        self.assertEqual(result, 100)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_data(), [100, 1, 20])
        result = self.integer_list.get_index(20)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    main()
