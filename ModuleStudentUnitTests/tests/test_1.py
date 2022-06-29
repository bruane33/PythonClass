import unittest
from class_definitions.student import Student as stu

class Test_test_1(unittest.TestCase):
    def setUp(self):
        self.student = stu("Finley","Chuck","Espionage Studies")

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "Chuck")
        self.assertEqual(self.student.last_name, "Finley")
        self.assertEqual(self.student.major,"Espionage Studies")

    def test_object_created_all_attributes(self):
        student = stu("Johnson", "Bob", "Puppetry", 3.6)
        assert student.first_name == "Bob"
        assert student.last_name == "Johnson"
        assert student.major == "Puppetry"
        assert student.gpa == 3.6

    def test_student_str(self):
        self.assertEqual(str(self.student),"Finley, Chuck has major Espionage Studies with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = stu("999", "Bob", "Business")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = stu("Johnson", "867", "Business")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = stu("Johnson", "Bob", "5309")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = stu("Johnson", "Bob", "Bizzness","Good")


if __name__ == '__main__':
    unittest.main()
