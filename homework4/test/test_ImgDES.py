import unittest

from homework4.ImgDES import encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        msg = b'HELLO DES'
        key = b'12345678'
        cph = encrypt(msg, key)
        self.assertEqual(msg, decrypt(cph, key))

        if __name__ == '__main__':
            unittest.main()
