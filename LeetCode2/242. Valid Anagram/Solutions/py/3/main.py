from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = defaultdict(int)

        for char_s, char_t in zip(s, t):
            char_count[char_s] += 1
            char_count[char_t] -= 1

        for _, value in char_count.items():
            if value != 0:
                return False
                
        return True
        