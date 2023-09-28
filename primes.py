"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def is_prime(n):
    if n <= 1:
        return False
    elif n > 1:
        #check for factors
        for i in range(2,n):
            if (n % i) == 0:
                return False
        return True
            
def primes(number_of_primes):
    list = []
    
    if number_of_primes <= 0:
        raise ValueError("Enter a positive integer")
    
    n = 2
    while len(list) < number_of_primes:
        if is_prime(n):
            list.append(n)
        n += 1

    return list
