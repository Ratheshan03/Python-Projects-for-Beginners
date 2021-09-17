def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """
    
    # your code here
    narciss = False
    sum = 0
    length = len(str(x))
 
    # Traversing through the string
    for i in str(x):
        # Converting character to int
        sum = sum + int(i) ** length
 
    # Converting string to integer
    number = int(x)
 
    # Comparing number and sum
    if (number == sum):
        narciss = True
    else:
         narciss = False
    
    return narciss
    

