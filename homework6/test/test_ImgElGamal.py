import unittest

from homework6 import elgamal
from homework6.ImgElGamal import encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        msg = b'HELLO ELGAMAL'

        keys = elgamal.generate_keys()
        priv = keys['privateKey']
        pub = keys['publicKey']

        cph = encrypt(msg, pub)
        self.assertEqual(msg, decrypt(cph, priv))

        if __name__ == '__main__':
            unittest.main()
