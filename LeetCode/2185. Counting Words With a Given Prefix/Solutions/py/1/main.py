class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # n = len(words)
        # m = len(pref)
        # Time Complexity:  O(n * m)
        # Space Complexity: O(1)
        
        total = 0
        for word in words:
            if len(pref) > len(word):
                continue
            for p, w in zip(pref, word):
                if p != w:
                    break
            else:
                total += 1
        return total