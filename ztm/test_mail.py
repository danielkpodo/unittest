import unittest
import mail_checker


class TestEmail(unittest.TestCase):
    def test_email(self):
        username1 = 'narh'
        age1 = 23
        username2 = 'naphtha'
        age2 = 26
        result1 = mail_checker.get_user_email(username1, age1)
        result2 = mail_checker.get_user_email(username2, age2)
        self.assertEqual(result1, 'narh.23@ymail.com')
        self.assertEqual(result2, 'naphtha.26@ymail.com')


if __name__ == "__main__":
    unittest.main()
