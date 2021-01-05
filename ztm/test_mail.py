import unittest
from mail_checker import get_user_email


class TestEmail(unittest.TestCase):
    def test_email(self):
        username = 'narh',
        age = 23
        result = get_user_email(username, age)
        self.assertEqual(result, "narh.23@gmail.com")

    