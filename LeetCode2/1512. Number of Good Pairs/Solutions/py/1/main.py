from collections import defaultdict

class Solution:
    
    def factorial(self, n: int):
        if n < 2:
            return 1
        total = n
        while n>1:
            total *= n-1
            n -= 1
        return total
            
  
    def get_binomial(self, n: int):
        if n < 3:
            return 1
        return (self.factorial(n))//(2*self.factorial(n-2))
      
  
    def numIdenticalPairs(self, nums: List[int]) -> int:
      hashmap = defaultdict(int)
      
      for n in nums:
        hashmap[n]+=1
        
      total = 0
        
      for k,v in hashmap.items():
        if v > 1:
            total += self.get_binomial(v)
        
      return total