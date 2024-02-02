from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char_s, char_t in zip(s, t):
            s_dict[char_s] += 1
            t_dict[char_t] += 1

        for s_key in s_dict.keys():
            if s_key not in t_dict:
                return False
            if s_dict[s_key] != t_dict[s_key]:
                return False

        return True
        