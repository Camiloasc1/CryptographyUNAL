import unittest

from homework5.ImgAES import encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        msg = b'HELLO AES'
        key16 = b'0123456789ABCDEF'
        key24 = b'0123456789ABCDEFGHIJKLMN'
        key32 = b'0123456789ABCDEFGHIJKLMNOPQRSTUV'

        cph = encrypt(msg, key16)
        self.assertEqual(msg, decrypt(cph, key16))

        cph = encrypt(msg, key24)
        self.assertEqual(msg, decrypt(cph, key24))

        cph = encrypt(msg, key32)
        self.assertEqual(msg, decrypt(cph, key32))

        if __name__ == '__main__':
            unittest.main()
