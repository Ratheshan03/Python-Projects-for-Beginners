# Checking if its a prime number or not

def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """
    
    # your code here
    prime_num = False
    
    if x > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(x/2)+1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime_num
            if (x % i) == 0:
                prime_num = False
                break
        else:
            prime_num = True
    else:
        prime_num = False
        
    return prime_num
