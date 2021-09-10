
def isTriangular(x):
    """Returns whether or not a given number x is triangular.
    
    The triangular number Tn is a number that can be represented in the form of a triangular 
    grid of points where the first row contains a single element and each subsequent row contains 
    one more element than the previous one.
    
    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.
    
    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)
    
    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """
    
    # your code here
    triangular = False
    if (x < 0):
        triangular = False
 
    # A Triangular number must be
    # sum of first n natural numbers
    sum, n = 0, 1
 
    while(sum <= x):
     
        sum = sum + n
        if (sum == x):
            triangular = True
        n += 1
 
    return triangular
            