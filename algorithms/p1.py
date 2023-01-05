import math
import sympy

from typing import List


def prime_factors(n: int) -> int:

    # defining base
    a = 2

    # defining exponent
    i = 2

    # iterate till a prime factor is obtained
    while(True):

        # recomputing a as required
        a = (a**i) % n
        print(a)

        # finding gcd of a-1 and n
        # using math function
        d = math.gcd((a-1), n)
        print('d:' + str(d))

        # check if factor obtained
        if (d > 1 and d < n):

            #return the factor
            return d

        # else increase exponent by one
        # for next round
        i += 1
        # if i > 10:
        #     return d
        # print('i=' + str(i))


def pollard_p1(n: int) -> List[int]:
    # list for storing prime factors
    facts = []

    # iterated till all prime factors
    # are obtained
    while(True):

        # function call
        d = prime_factors(n)
        print(d)

        # add obtained factor to list
        facts.append(d)

        # reduce n
        r = int(n/d)
        print(r)

        # check for prime using sympy
        if(sympy.isprime(r)):

            # both prime factors obtained
            facts.append(r)

            break

        # reduced n is not prime, so repeat
        else:
            n = r

    return facts
