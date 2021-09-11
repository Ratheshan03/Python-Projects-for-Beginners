#  Factors of a given number

def factors(x):
    factor_lst = []
    for i in range(1,x+1):
        if (x % i == 0 ):
            factor_lst.append(i)
    return factor_lst

print(factors(21))
