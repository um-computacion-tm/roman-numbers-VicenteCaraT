import unittest

from test_decimal_a_romano import decimal_to_roman
from test_romano_a_decimal import roman_to_decimal

#decimal a romano

class TestDecimalToRoman(unittest.TestCase):

    def test_uno(self):

        resultado= decimal_to_roman (1)

        self.assertEqual (resultado, 'I')

    def test_dos(self):

        resultado = decimal_to_roman(2)

        self.assertEqual (resultado,"II")

    def test_tres(self):

        resultado = decimal_to_roman(3)

        self.assertEqual (resultado, "III")

    def test_cuatro(self):

        resultado = decimal_to_roman (4)

        self.assertEqual (resultado, "IV")

    def test_cinco(self):

        resultado = decimal_to_roman(5)

        self.assertEqual (resultado,"V")

    def test_seis(self):

        resultado = decimal_to_roman(6)

        self.assertEqual(resultado, "VI")

    def test_diez(self):

        resultado = decimal_to_roman (10)

        self.assertEqual (resultado,"X")

    def test_veinte(self):

        resultado = decimal_to_roman(20)

        self.assertEqual (resultado,"XX")

    def test_cincuentayseis(self):

        resultado = decimal_to_roman(56)

        self.assertEqual (resultado, "LVI")
    
    def test_cientoveintitres(self):

        resultado = decimal_to_roman(123)

        self.assertEqual (resultado, 'CXXIII')
    
    def test_docientosveinte(self):
        
        resultado = decimal_to_roman(220)

        self.assertEqual(resultado, 'CCXX')
    
    def test_cuatrocientosobhentayuno(self):

        resultado = decimal_to_roman(481)

        self.assertEqual(resultado, 'CDLXXXI')
    
    def test_quinientos(self):

        resultado = decimal_to_roman(500)

        self.assertEqual(resultado, 'D')
    
    def test_setecientossetentaycuatro(self):

        resultado = decimal_to_roman(774)

        self.assertEqual(resultado, 'DCCLXXIV')
    
    def test_ochocientossetentaysiente(self):

        resultado= decimal_to_roman(877)

        self.assertEqual(resultado, 'DCCCLXXVII' )
    
    def test_mil(self):

        resultado = decimal_to_roman(1000)

        self.assertEqual(resultado, 'M')


#romano a decimal


    def test_I(self):
    
        resu = (roman_to_decimal('I'))

        self.assertEqual(resu, 1)
    
    def test_II(self):
        
        resu = (roman_to_decimal('II'))

        self.assertEqual(resu, 2)
    
    def test_III(self):

        resu = (roman_to_decimal('III'))

        self.assertEqual(resu, 3)

    def test_IV(self):
        
        resu = (roman_to_decimal('IV'))

        self.assertEqual(resu, 4)
                
    def test_V(self):

        resu = (roman_to_decimal('V'))

        self.assertEqual(resu, 5)

    def test_VI(self):

        resu = (roman_to_decimal('VI'))

        self.assertEqual(resu, 6)

    def test_VIII(self):

        resu = (roman_to_decimal('VIII'))

        self.assertEqual(resu, 8)

    def test_X(self):

        resu = (roman_to_decimal('X'))

        self.assertEqual(resu, 10)

    def test_XV(self):

        resu = (roman_to_decimal('XV'))

        self.assertEqual(resu, 15)

    def test_XX(self):

        resu = (roman_to_decimal('XX'))

        self.assertEqual(resu, 20)



if __name__ == '__main__':
    unittest.main()