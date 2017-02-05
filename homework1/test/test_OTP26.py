import unittest

from homework1.OTP26 import int_to_alpha_map, code, decode, keyof


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(26, len(int_to_alpha_map))
        self.assertEqual('QJKES', code('TODAY', 'XVHEU'))
        self.assertEqual('TODAY', decode('QJKES', 'XVHEU'))
        self.assertEqual('XVHEU', keyof('TODAY', 'QJKES'))


if __name__ == '__main__':
    unittest.main()
