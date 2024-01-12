class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))
        return s_sorted == t_sorted