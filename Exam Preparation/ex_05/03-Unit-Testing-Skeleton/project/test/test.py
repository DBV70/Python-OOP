from project.climbing_robot import ClimbingRobot
from unittest import TestCase, main

class TestClimbingRobotClass(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'TestPart', 100, 200)

    def test_init(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('TestPart', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = 'InvalidCategory'
        self.assertEqual("Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ex.exception))
        self.robot.category = 'Indoor'
        self.assertEqual('Indoor', self.robot.category)

    def test_get_used_capacity(self):
        self.robot.installed_software = [{'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}]
        self.assertEqual(30, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.assertEqual(100, self.robot.get_available_capacity())
        self.robot.installed_software = [{'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}]
        self.assertEqual(70, self.robot.get_available_capacity())

    def test_get_used_memory(self):
        self.robot.installed_software = [{'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}]
        self.assertEqual(50, self.robot.get_used_memory())

    def test_get_available_memory(self):
        self.assertEqual(200, self.robot.get_available_memory())
        self.robot.installed_software = [{'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}]
        self.assertEqual(150, self.robot.get_available_memory())

    def test_install_software(self):
        software = {'name': 'Software1', 'capacity_consumption': 40, 'memory_consumption': 70}
        result = self.robot.install_software(software)
        self.assertEqual([{'name': 'Software1', 'capacity_consumption': 40, 'memory_consumption': 70}], self.robot.installed_software)
        self.assertEqual(f"Software 'Software1' successfully installed on Mountain part.", result)
        software = {'name': 'Software2', 'capacity_consumption': 140, 'memory_consumption': 170}
        result = self.robot.install_software(software)
        self.assertEqual([{'name': 'Software1', 'capacity_consumption': 40, 'memory_consumption': 70}], self.robot.installed_software)
        self.assertEqual(f"Software 'Software2' cannot be installed on Mountain part.", result)

if __name__ == '__main__':
    main()
