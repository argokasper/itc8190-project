'''
Main class for collecting all Pollards algorithms
'''
from typing import List

from algorithms.p1 import pollard_p1
from algorithms.rho import pollard_rho

def print_intro():
    print("######################################################")
    print("######################  WELCOME  #####################")
    print("######################################################")
    print()
    print("This small application will give you Pollalrd's p-1")
    print("and Pollald's rho factorisations of a chosen number.")
    print()
    print("######################################################")
    print("NB! It will only accept integers. If you accidentally")
    print("entered a decimal it will be floored down to an integer.")
    print("######################################################")
    print()
    print("Let\'s begin!")
    print()

def print_results(number: int, p1_facts: List[int] = None, rho_facts: List[int] = None, p1_facts_error: bool = False, rho_facts_error: bool = False):
    print("######################################################")
    print("###############  RESULTS ARE HERE!!  #################")
    print("######################################################")
    print()

    print('For your chosen number: ' + str(number))

    if p1_facts_error:
        print('Pollards\'s p-1 factorisation is not possible!')
    else:
        print('Pollards\'s p-1 factorisation gives us: ' + ', '.join(map(str, p1_facts)))

    if rho_facts_error:
        print('Pollards\'s rho factorisation is not possible!')
    else:
        print('Pollards\'s rho factorisation gives us: ' + ', '.join(map(str, rho_facts)))

def main():
    print_intro()

    reply = input('Do you wish to continue? (y/n)')
    if reply.lower() != 'y':
        print('You chose not to pursue factorisation this time. Maybe you can do so next time.')
        exit()

    try:
        raw_number = input('Enter your number: ')
        number = int(float(raw_number))
    except:
        print('You did not enter a number')
        exit(1)

    if float(raw_number) != float(number):
        print('You specified a decimal and now it got converted into an integer, integer value=' + str(number))

    p1_facts_error = False
    rho_facts_error = False
    try:
        p1_facts = pollard_p1(number)
    except:
        p1_facts_error = True

    try:
        rho_facts = pollard_rho(number)
    except:
        rho_facts_error = True

    print_results(number, p1_facts, rho_facts, p1_facts_error, rho_facts_error)



if __name__ == "__main__":
    main()
