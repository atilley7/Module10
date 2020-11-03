import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student("Tilley", "Avery", 'Business', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Tilley')
        self.assertEqual(self.student.first_name, 'Avery')
        self.assertEqual(self.student.major, 'Business')

    def test_object_created_all_attributes(self):
        student = s.Student('Tilley', 'Avery', 'Business', 4.0)
        assert student.last_name == 'Tilley'
        assert student.first_name == 'Avery'
        assert student.major == 'Business'
        assert student.gpa == 4.0


if __name__ == '__main__':
    unittest.main()
