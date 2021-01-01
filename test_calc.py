import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 90)
        self.assertEqual(result, 100)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-10, -30), -40)


# helps  us run our test_case.py file via the unittest module
unittest.main()
