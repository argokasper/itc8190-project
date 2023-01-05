'''
Pollard\'s p-1 algorithm class
'''

from math import gcd
import sympy

from typing import List

MAX_RETRIES = 100


def prime_factors(number: int) -> int:
    '''Obtains a prime factor for a given number or throws an exception

    Args:
        number (int): number to start looking a factor for

    Returns:
        int: prime factor
    '''

    # a=coprime to number
    coprime = 2
    # M value, this is trivial, thus chosen as 2 which increments each loop
    m = 2

    # iterate till a prime factor is obtained
    for m in range(2, MAX_RETRIES):
        # recomputing a=coprime as required to save memory
        coprime = (coprime**m) % number

        # finding gcd of coprime-1 and number
        potent_fact = gcd((coprime-1), number)

        # check if factor obtained
        if potent_fact > 1 and potent_fact < number:
            return potent_fact

        # else increase exponent(M) by one
        # for next round
        m += 1

    if m == MAX_RETRIES:
        raise Exception('Failure! gcd()=1')


def pollard_p1(number: int) -> List[int]:
    '''Finds two factors for a number or throws an exception if not.

    Args:
        number (int): chosen number

    Returns:
        List[int]: factors as an array
    '''

    # list for storing prime factors
    factors = []

    # iterated till all prime factors are found or throw an exception
    while(True):
        factor = prime_factors(number)
        factors.append(factor)

        # reduce n
        other_factor = int(number / factor)

        if sympy.isprime(other_factor):
            factors.append(other_factor)
            break
        # not prime, so repeat
        else:
            number = other_factor

    return factors
