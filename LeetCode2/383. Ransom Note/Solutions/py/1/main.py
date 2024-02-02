from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       # n = len(ransomNote)
       # m = len(magazine)
       # Time Complexity:  O(m)
       # Space Complexity: O(26) = O(1)

       hashtable = defaultdict(int) 

       for char in ransomNote:
           hashtable[char] += 1
        
       for char in magazine:
           if char in hashtable:
                hashtable[char] -= 1
                if hashtable[char] == 0:
                    hashtable.pop(char)

       return not hashtable

        