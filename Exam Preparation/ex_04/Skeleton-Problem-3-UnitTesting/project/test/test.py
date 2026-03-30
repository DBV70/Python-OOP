from project.senior_student import SeniorStudent
from unittest import TestCase, main

class SeniorStudentTests(TestCase):
    def setUp(self):
        self.student = SeniorStudent('12345', 'John', 100.0)

    def test_init(self):
        self.assertEqual('12345', self.student.student_id)
        self.assertEqual('John', self.student.name)
        self.assertEqual(100.0, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_student_id_setter(self):
        self.student.student_id = '1234'
        self.assertEqual('1234', self.student.student_id)
        with self.assertRaises(ValueError) as ex:
            self.student.student_id = '123'
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_name_setter(self):
        self.student.name = 'Jane'
        self.assertEqual('Jane', self.student.name)
        with self.assertRaises(ValueError) as ex:
            self.student.name = ''
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_student_gpa_setter(self):
        self.student.student_gpa = 10.5
        self.assertEqual(10.5, self.student.student_gpa)
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = 0.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_apply_to_college(self):
        self.student.student_gpa = 2.0
        self.assertEqual('Application failed!', self.student.apply_to_college(10, 'College of Music'))
        self.student.student_gpa = 100.0
        self.assertEqual('John successfully applied to College of Music.', self.student.apply_to_college(10, 'College of Music'))
        self.assertEqual('COLLEGE OF MUSIC', self.student.colleges.pop())

    def test_update_gpa(self):
        self.assertEqual('The GPA has not been changed!', self.student.update_gpa(0))
        self.assertEqual('Student GPA was successfully updated.', self.student.update_gpa(100))
        self.assertEqual(100.0, self.student.student_gpa)

    def test_eq(self):
        student2 = SeniorStudent('6789', 'Jane', 85.0)
        self.assertTrue(self.student.__eq__(self.student))
        self.assertFalse(self.student.__eq__(student2))

if __name__ == '__main__':
    main()
