import unittest


def roman_to_decimal(romano):
    d_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000}
    d_decimal= [d_num[char] for char in romano] #char=variable temporal para iterar
    total = 0
    for i in range(len(d_decimal)):
        if i == len(d_decimal) -1 or d_decimal[i] >= d_decimal[i+1]:
            total += d_decimal[i]
        else:
            total -= d_decimal[i]
    return total

        


class RomanToDecimal (unittest.TestCase):
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
if __name__ == "__main__":
    unittest.main()