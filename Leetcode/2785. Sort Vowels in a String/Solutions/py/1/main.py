class Solution:
    def sortVowels(self, s: str) -> str:
       # n = len(s)
       # m = len(vowals)
       # Time Complexity:  O(m * log(m))
       # Space Complexity: O(n)
       
       vowels = [char for char in s if char.lower() in "aeiou"] 
       vowels.sort()
       vowels = iter(vowels)
       t = []
       for i in range(len(s)):
           char = s[i]
           if char.lower() in "aeiou":
               char = next(vowels)
           t.append(char)

       return "".join(t)