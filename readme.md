# Pollard's p-1 and Pollard's rho factorisation algorithms

## Requirements
* Python v3.10 or greater (was developed using v3.10.2)
* Command line (Command Prompt/Powershell or Terminal)

## How does it work
1. Clone this repo.
2. Open the cloned repo folder in command line.
3. Install required packages: `pip install -r requirements.txt` or `py -m pip install -r requirements.txt`
3. Type: `py ./main.py`
4. Follow on-screen instructions and learn the results of these two factorisation algorithms.

### Complexity of these algorithms
| Both functions (`pollard_p1` and `pollard_rho`) are in the *pseudo polynomial* complexity class because of the python code is represented in binary numbers and with increasing numbers the underlying complexity increases exponentially.
From the functional complexity the complexities in Big-O notation are as follows:
* `pollard_p1()`: O(√n)
* `pollard_rho()`: O(√n*logn)



### Examples of Pollard's p-1 factorisation
* The factors of 6 are 3 and 2.
* The factors of 273 are 3, 7 and 13.
* The factors of 116,393 are 487 and 239.
* The factors of 3,789,829 are 1181 and 3209.
* The factors of 7,388,399 are 3571 and 2069.
* The factors of 392,524,199 are 991, 919 and 431.
* The factors of 5,467,658,333,345 are 1105, 967 and 5116967.

### Examples of Pollard's rho factorisation
* The factor of 9 is 3.
* The factor of 273 is 21.
* The factor of 116,396 is 2.
* The factor of 3,789,829 is 1181.
* The factor of 4,294,967,297 is 641.
* The factor of 5,467,658,333,345 is 5.

## References
* For Pollard's p-1 algorithm inspiration:
    * https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm
    * https://www.geeksforgeeks.org/pollard-p-1-algorithm/
* For Pollard's rho algorithm inspiration:
    * https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    * https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/
