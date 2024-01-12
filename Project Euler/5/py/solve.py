"""
Link: https://projecteuler.net/problem=5

Answer:  232792560

"""

__author__ = "El Mazaz Badr"

import math


def is_divisible(n: int, d: int) -> bool:
    return n % d == 0


def bruteforce():
    n = 2520
    while True:
        print("Trying: ", end="")
        print(n, end="\r")
        for i in range(1, 21):
            if not is_divisible(n, i):
                break
        else:
            break
        n+=1
        
    print("Solution: ", n)
    
    
def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
        
def is_divisible(n: int, d: int) -> bool:
    return n % d == 0


def get_divisible_primes(number: int) -> list[int]:
    if number < 1:
        return []
    if is_prime(number):
        return [number]
    factors = []
    i = 2
    while number != 1:
        if is_divisible(number, i) and is_prime(i):
            factors.append(i)
            number = number // i
            i=2
            continue
        i+=1
    return factors
        
    

    
def main():
    for i in range(2, 21):
        print(i, get_divisible_primes(i))
    
    numbers = range(2, 21)
    primes = [get_divisible_primes(x) for x in numbers]
    unique = {}
    for p in primes:
        for n in p:
            unique[n] = 0
            
    for u in unique.keys():
        exp = 0
        for p in primes:
            tmp = p.count(u)
            if tmp > exp:
                exp = tmp
                unique[u] = tmp
                
                
    print("unique", unique)
    
    ans = 1
    for k in unique.keys():
        ans *= int(math.pow(k, unique[k]))
        
    print("Solution:", ans)
            
    




if __name__ == "__main__":
    #bruteforce()
    main()