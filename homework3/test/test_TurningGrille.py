import unittest

from homework3.TurningGrille import holes_to_matrix, pad_crop_message, matrix_to_message, rotate, unrotate, encrypt, \
    decrypt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([[False, False], [True, False]], rotate([[True, False], [False, False]]))
        self.assertEqual([[False, False], [False, True]], rotate([[False, False], [True, False]]))
        self.assertEqual([[False, True], [False, False]], rotate([[False, False], [False, True]]))
        self.assertEqual([[True, False], [False, False]], rotate([[False, True], [False, False]]))

        self.assertEqual([[False, True], [False, False]], unrotate([[True, False], [False, False]]))
        self.assertEqual([[False, False], [False, True]], unrotate([[False, True], [False, False]]))
        self.assertEqual([[False, False], [True, False]], unrotate([[False, False], [False, True]]))
        self.assertEqual([[True, False], [False, False]], unrotate([[False, False], [True, False]]))

        size = 4
        key = holes_to_matrix([0, 9, 11, 14], size)
        msg = "JIMATTACKSATDAWN"
        cph = "JKTDSAATWIAMCNAT"
        self.assertEqual(cph, encrypt(msg, key, size, rotate))
        self.assertEqual(msg, decrypt(cph, key, size, rotate))

        size = 9
        key = holes_to_matrix([0, 3, 5, 11, 17, 19, 24, 29, 31, 34, 40, 42, 44, 48, 52, 54, 59, 64, 67, 71, 74], size)
        msg = "THISISAMESSAGETHATIAMENCRYPTINGSWITHATURNINGGRILLETOSPROVIDETHISILLUSTRATSIVEEXAMPLE"
        cph = "TESHNINCIGLSRGYLRIUSPITSATLILMREENSATTOGSIAWGIPVERTOTEHHVAEAXITDTUAIMERANPMTLHIEI"
        self.assertEqual(msg, decrypt(cph, key, size, rotate))
        self.assertEqual(cph, encrypt(msg, key, size, rotate))


if __name__ == '__main__':
    unittest.main()
