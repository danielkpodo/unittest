import unittest
from employees import Employee


class TestEmployee(unittest.TestCase):
    emp_1 = Employee("narh", "kpodo", 80)
    emp_2 = Employee("nelson", "mandela", 800)

    def test_email(self):
        self.assertEqual(self.emp_1.email, "narhkpodo@gmail.com")
        self.assertEqual(self.emp_2.email, "nelsonmandela@gmail.com")


unittest.main()
