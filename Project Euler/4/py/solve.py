"""

Link: https://projecteuler.net/problem=4

Answer:  906609

"""

__author__ = "El Mazaz Badr"

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

def main():
    maximum = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if product < maximum:
                break
            if is_palindrome(product):
                maximum = product
                break
    print("Solution: ", maximum)

if __name__ == "__main__":
    main()