import unittest
import main


class TestMain(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(main.addNumbers(12, 10), 22)


unittest.main()
