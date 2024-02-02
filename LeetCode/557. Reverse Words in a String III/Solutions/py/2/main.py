class Solution:
    def reverseWords(self, s: str) -> str:
       # n = len(s)
       # Time Complexity:  O(n)
       # Space Complexity: O(n)

       return " ".join([word[::-1] for word in s.split()]) 