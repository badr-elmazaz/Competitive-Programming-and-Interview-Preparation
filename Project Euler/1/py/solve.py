"""
Link: https://projecteuler.net/problem=1

Answer:  233168

"""

__author__ = "El Mazaz Badr"

def main():
  sum = 5
  
  for i in range(3, 1000, 3):
    sum+=i
    if i % 5 == 0:
      sum+=(i-5)+(i+5)
      
  print("Solution:", sum)


if __name__ == "__main__":
    main()