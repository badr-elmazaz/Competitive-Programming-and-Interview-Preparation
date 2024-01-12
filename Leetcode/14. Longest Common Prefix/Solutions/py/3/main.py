class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # n = len(strs) ; m = len(min(strs))
        # time  -> O(n*m)
        # space -> O(m)

        for i in range(len(strs[0])): # time -> O(m)
            char_to_check = strs[0][i]
            for j in range(1, len(strs)): # time -> O(n)
                if i == len(strs[j]) or strs[j][i] != char_to_check:
                    return strs[0][:i] # space -> O(m)
        return strs[0]
            