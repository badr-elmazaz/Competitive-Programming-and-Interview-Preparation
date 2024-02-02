class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # n = len(s)
        # m = len(t)
        # Time Complexity:  O(t)
        # Space Complexity: O(1)
        
        s_idx = 0
        for char_t in t:
            if s_idx == len(s):
                break
            char_s = s[s_idx]
            if char_t == char_s:
                s_idx += 1

        return s_idx == len(s)