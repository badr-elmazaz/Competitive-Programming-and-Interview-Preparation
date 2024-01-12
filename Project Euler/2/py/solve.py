"""
Link: https://projecteuler.net/problem=2

Answer:  4613732

"""

__author__ = "El Mazaz Badr"

import math

def is_prime(n: int) -> bool:
    
    for i in range(2, math.ceil(math.sqrt(n))):
        if n%i == 0:
            return False
    return True


def main():
    LIMIT=600851475143
    ans=1
    
    for i in range(LIMIT-1, 0, -1):
        if LIMIT%i == 0 and is_prime(i): 
            ans=i
            break
    
    print("Solution:", ans)

if __name__ == "__main__":
    main()