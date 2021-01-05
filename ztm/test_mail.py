import unittest
import mail_checker


class TestEmail(unittest.TestCase):
    def test_email(self):
        username = 'narh'
        age = 23
        result = mail_checker.get_user_email(username, age)
        self.assertEqual(result, 'narh.23@gmail.com')


if __name__ == "__main__":
    unittest.main()
