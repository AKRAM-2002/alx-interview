#!/usr/bin/python3
"""
0-minOperations.py

"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def minOperations(n):
    """
    Calculate the minimum number of operations (Copy All and Paste) required 
    to achieve exactly n 'H' characters in the text editor.
    
    Args:
    n (int): The target number of 'H' characters.
    
    Returns:
    int: The fewest number of operations to reach n 'H' characters. 
         If n is impossible, return 0.
    """
    if n <= 1:
        # If n is 1 or less, it's impossible or already at the target.
        return 0
    
    operations = 0
    divisor = 2
    
    # Factorizing n by its smallest divisors
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            # Add the divisor to operations (since we need that many steps)
            operations += divisor
            # Reduce n by dividing it by the divisor
            n //= divisor
        # Move to the next potential divisor
        divisor += 1
    
    return operations
