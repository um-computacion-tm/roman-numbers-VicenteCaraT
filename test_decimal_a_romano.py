

import unittest




def decimal_to_roman (decimal):

    if decimal == 1:
        return "I"
    if decimal == 2:
        return "I" * 2
    if decimal == 3:
        return "I" * 3


    



class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):

        resultado= decimal_to_roman (1)

        self.assertEqual (resultado, "I")

    def test_2 (self):

        resultado = decimal_to_roman(2)

        self.assertEqual (resultado,"II")

    def test_3(self):

        resultado = decimal_to_roman(3)

        self.assertEqual (resultado, "III")

    def test_4(self):

        resultado = decimal_to_roman (4)

        self.assertEqual (resultado, "IV")

    def test_5 (self):

        resultado = decimal_to_roman(5)

        self.assertEqual (resultado,"V")

    def test_6 (self):

        resultado = decimal_to_roman(6)

        self.assertEqual(resultado, "VI")

    def test_10(self):

        resultado = decimal_to_roman (10)

        self.assertEqual (resultado,"X")

    def test_20(self):

        resultado = decimal_to_roman(20)

        self.assertEqual (resultado,"XX")

    def test_56 (self):

        resultado = decimal_to_roman(56)

        self.assertEqual (resultado, "LVI")


if __name__ == "__main__":
    unittest.main()
