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


#  Returning unique list

def Uniques(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list

print(Uniques([1,2,3,4,2,4,5,3,2,1,5,5]))


# 
