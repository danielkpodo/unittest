import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 90)
        self.assertEqual(result, 100)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-10, -30), -40)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 2), 4)
        self.assertEqual(calc.multiply(10, 0), 0)
        self.assertEqual(calc.multiply(100, 10), 1000)

    def test_substract(self):
        self.assertEqual(calc.substract(100, 50), 50)
        self.assertEqual(calc.substract(90, 60), 30)

    def test_divide(self):
        self.assertEqual(calc.divide(100, 2), 50)
        self.assertEqual(calc.divide(10, 10), 1)

        # testing exceptions
        with self.assertRaises(ValueError):
            calc.divide(10, 2)


# helps  us run our test_case.py file via the unittest module
unittest.main()
