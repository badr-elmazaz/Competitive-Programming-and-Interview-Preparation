class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # n = len(strs) ; m = len(max(strs))
        # time  -> O(n*m)
        # space -> O(m)

        shortes_str_len = len(strs[0])
        for i in range(1, len(strs)):
            shortes_str_len = len(strs[i]) if len(strs[i]) < shortes_str_len else shortes_str_len
        prefix = ""
        for i in range(shortes_str_len): # O(m)
            char_to_check = strs[0][i]
            for j in range(1, len(strs)): # O(n)
                if strs[j][i] != char_to_check:
                    break
            else:
                prefix += char_to_check
                continue
            break
            
        return prefix
            