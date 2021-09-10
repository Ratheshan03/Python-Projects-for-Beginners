def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """
    
    # your code here
    composite = False
    
    factor=0
    for i in range(1,x):
        if x%i==0:
            factor = i
    if factor > 1:
        composite = True 
    elif x == 1:
        composite = False
    else:
        composite = False
    
    return composite 
