#  Reverse Words

def ReverseWords(string):
    result = ""
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result


print(ReverseWords("APPLE"))


#  Factors of a given number

def factors(x):
    factor_list = []
    for i in range(1,x+1):
        if (x % i == 0 ):
            factor_list.append(i)
    return factor_list

print(factors(21))