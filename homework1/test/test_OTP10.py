import unittest

from homework1.OTP10 import mod10_map, alpha_to_int, int_to_alpha, code, decode, keyof


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(30, len(mod10_map))
        self.assertEqual([0, 2, 0, 6, 0], alpha_to_int('ABP'))
        self.assertEqual('ABP', int_to_alpha([0, 2, 0, 6, 0]))


if __name__ == '__main__':
    unittest.main()
