import unittest

from homework2.Hill import encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('DELW', encrypt('JULY', [11, 8, 3, 7], 2))
        self.assertEqual('JULY', decrypt('DELW', [11, 8, 3, 7], 2))

        self.assertEqual('JULY', encrypt('DELW', [7, -8, -3, 11], 2))
        self.assertEqual('DELW', decrypt('JULY', [7, -8, -3, 11], 2))

        self.assertEqual('NUMBERTHEORYISEASY', encrypt('VKFZRVWTIAZSMISGKA', [7, -8, -3, 11], 2))
        self.assertEqual('NUMBERTHEORYISEASY', decrypt('VKFZRVWTIAZSMISGKA', [11, 8, 3, 7], 2))


if __name__ == '__main__':
    unittest.main()
