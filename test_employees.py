import unittest
from employees import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee("narh", "kpodo", 80)
        emp_2 = Employee("nelson", "mandela", 800)
        self.assertEqual(emp_1.email, "narhkpodo@gmail.com")
        self.assertEqual(emp_2.email, "nelsonmandela@gmail.com")

    def test_fullname(self):
        emp_1 = Employee("narh", "kpodo", 320)
        emp_2 = Employee("nelson", "mandela", 90)

        self.assertEqual(emp_1.fullname, "narh kpodo")
        self.assertEqual(emp_2.fullname, "nelson mandela")


unittest.main()
