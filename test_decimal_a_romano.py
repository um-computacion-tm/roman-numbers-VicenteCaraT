



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

if __name__ == "__main__":
    pass
