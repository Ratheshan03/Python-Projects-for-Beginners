
#  Returning unique list

def Uniques(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list

print(Uniques([1,2,3,4,2,4,5,3,2,1,5,5]))


