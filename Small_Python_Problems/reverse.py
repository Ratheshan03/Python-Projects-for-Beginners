#  Reverse Words

def ReverseWords(string):
    result = ""
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result


print(ReverseWords("APPLE"))