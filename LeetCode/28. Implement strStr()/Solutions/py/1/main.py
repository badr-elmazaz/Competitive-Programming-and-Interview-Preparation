class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # n = len(haystack) ; m = len(needle)
        # time  -> O(n*m)
        # space -> O(1)
        
        for i in range(len(haystack)-len(needle)+1): # time -> O(n)
            k = i
            for j in range(len(needle)): # time -> O(m)
                if haystack[k] != needle[j]:
                    break
                k += 1
            else:
                return i
        return -1
        