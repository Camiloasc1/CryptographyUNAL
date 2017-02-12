import unittest

from homework2.Hill import encrypt, decrypt, is_valid_key


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('DELW', encrypt('JULY', [11, 8, 3, 7], 2))
        self.assertEqual('JULY', decrypt('DELW', [11, 8, 3, 7], 2))

        self.assertEqual('JULY', encrypt('DELW', [7, -8, -3, 11], 2))
        self.assertEqual('DELW', decrypt('JULY', [7, -8, -3, 11], 2))

        self.assertEqual('NUMBERTHEORYISEASY', encrypt('VKFZRVWTIAZSMISGKA', [7, -8, -3, 11], 2))
        self.assertEqual('NUMBERTHEORYISEASY', decrypt('VKFZRVWTIAZSMISGKA', [11, 8, 3, 7], 2))

        self.assertEqual('CMSF', encrypt('ASDF', [1, 2, 3, 5], 2))
        self.assertEqual('ASDF', decrypt('CMSF', [1, 2, 3, 5], 2))

        self.assertEqual('ASDF', encrypt('CMSF', [-5, 2, 3, -1], 2))
        self.assertEqual('CMSF', decrypt('ASDF', [-5, 2, 3, -1], 2))

        self.assertEqual(False, is_valid_key([1, 2, 3, 4]))
        self.assertEqual(False, is_valid_key([1, 3, 5, 7]))
        self.assertEqual(True, is_valid_key([11, 8, 3, 7]))
        self.assertEqual(True, is_valid_key([7, -8, -3, 11]))
        self.assertEqual(True, is_valid_key([1, 2, 3, 5]))
        self.assertEqual(True, is_valid_key([-5, 2, 3, -1]))


if __name__ == '__main__':
    unittest.main()
