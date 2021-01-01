import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 90)
        self.assertEqual(result, 100)


unittest.main()
