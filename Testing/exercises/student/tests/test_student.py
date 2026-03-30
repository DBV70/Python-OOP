from project.student import Student
from unittest import TestCase, main

class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("Ivan")

    def test_init(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_course_exist(self):
        self.student.courses["Math"] = []
        result = self.student.enroll("Math", ["Note 1", "Note 2"], "")
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_not_exist_with_notes_Y(self):
        result = self.student.enroll("Math", ["Note 1", "Note 2"], "Y")
        self.assertEqual("Math", list(self.student.courses.keys())[0])
        self.assertEqual(["Note 1", "Note 2"], self.student.courses["Math"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_not_exist_with_notes_(self):
        result = self.student.enroll("Math", ["Note 1", "Note 2"], "")
        self.assertEqual("Math", list(self.student.courses.keys())[0])
        self.assertEqual(["Note 1", "Note 2"], self.student.courses["Math"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_not_exist_without_notes(self):
        result = self.student.enroll("Math", [], "N")
        self.assertEqual("Math", list(self.student.courses.keys())[0])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_course_exist(self):
        self.student.courses["Math"] = []
        result = self.student.add_notes("Math", "Note 1")
        self.assertEqual("Note 1", self.student.courses["Math"][0])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_course_not_exist_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Math", "Note 1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_exist(self):
        self.student.courses["Math"] = []
        result = self.student.leave_course("Math")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_not_exist_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()
