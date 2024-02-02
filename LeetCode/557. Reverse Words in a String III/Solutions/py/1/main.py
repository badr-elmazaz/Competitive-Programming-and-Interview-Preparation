class Solution:
    def reverseWords(self, s: str) -> str:
       # n = len(s)
       # Time Complexity:  O(n)
       # Space Complexity: O(1)

       left = right = 0

       s = list(s) # Time Complexity: O(n)

       while right < len(s): # Time Complexity: O(n)

           if right == (len(s) - 1) or s[right + 1] == " ":
               j = right
               for i in range(left, (left + right + 1) // 2):
                   s[i], s[j] = s[j], s[i]
                   j -= 1
               left = right + 2
           right += 1

       return "".join(s) # Time: Complexity: O(n)


         