class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # n = len(strs) ; m = len(max(strs))
        # time  -> O(n*m)
        # space -> O(m)

        shortes_str_len = len(min(strs, key=len)) # space -> O(1)
        prefix = ""
        for i in range(shortes_str_len): # time -> O(m)
            char_to_check = strs[0][i]
            for j in range(1, len(strs)): # time -> O(n)
                if strs[j][i] != char_to_check:
                    break
            else:
                prefix += char_to_check
                continue
            break
            
        return prefix
            