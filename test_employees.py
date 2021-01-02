import unittest
from employees import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee("narh", "kpodo", 80)
        self.emp_2 = Employee("nelson", "mandela", 800)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "narhkpodo@gmail.com")
        self.assertEqual(self.emp_2.email, "nelsonmandela@gmail.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "narh kpodo")
        self.assertEqual(self.emp_2.fullname, "nelson mandela")

    def test_raise(self):
        self.assertEqual(self.emp_1.apply_raise, 160)
        self.assertEqual(self.emp_2.apply_raise, 1600)


unittest.main()
