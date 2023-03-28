
import unittest


'''Letras en los numeros romano I, V, X, L, C, D, M'''


    


def decimal_to_roman (entero):

    lts_m = ['','M'] #generar lista mill
    lts_c = ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] #generar lista centena
    lts_d = ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] #generar lista decimos
    lts_u = ['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] #generar lista unidades

    milli = lts_m [entero // 1000] 
    centena = lts_c [(entero % 1000) // 100] 
    decena = lts_d [(entero % 100) // 10]
    unidad = lts_u [entero % 10]

    resultado = (milli + centena + decena + unidad)

    

    return resultado

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
        


if __name__ == "__main__":
    unittest.main()
