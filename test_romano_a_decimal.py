

def roman_to_decimal(romano):
    d_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000}
    d_decimal= [d_num[n] for n in romano] #n=variable temporal para iterar
    total = 0
    for i in range(len(d_decimal)):
        if i == len(d_decimal) -1 or d_decimal[i] >= d_decimal[i+1]:
            total += d_decimal[i]
        else:
            total -= d_decimal[i]
    return total

if __name__ == "__main__":
    pass