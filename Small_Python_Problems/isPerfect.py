def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    
    # your code here
    
    perfect_num = False
    sum = 0
    for i in range(1, x):
        if(x % i == 0):
            sum += i
    if (sum == x):
        perfect_num = True
        
    else:
        perfect_num = False
        
    return perfect_num