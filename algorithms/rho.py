'''
Pollard\'s rho algorithm class
'''
from random import randint
from math import gcd

def modular_pow(base: int, exponent: int, modulus: int) -> int:

    result = 1

    while exponent > 0:
        # if y is odd, multiply base with result
        if exponent & 1:
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result

def pollard_rho(number: int) -> int:
    '''Gives us one nontrivial factor for a given number

    Args:
        n (int): Given number

    Returns:
        int: A factor for a numer
    '''
    # no prime factor for 1
    if number == 1:
        return number

    # if number is even, one factor is 2
    if number % 2 == 0:
        return 2

    # initialising required variables
    x = randint(0, 2) % (number - 2) # x is in the range [2, N)
    y = x
    c = randint(0, 1) % (number - 1)
    d = 1

    while d == 1:
        # f(x(i))
        x = (modular_pow(x, 2, number) + c + number) % number

        # f(f(y(i)))
        y = (modular_pow(y, 2, number) + c + number) % number
        y = (modular_pow(y, 2, number) + c + number) % number

        # gcd of |x-y| and number
        d = gcd(abs(x - y), number)

        # retry if the algorithm fails to find prime factor
        if (d == number):
            return pollard_rho(number)

    return d
