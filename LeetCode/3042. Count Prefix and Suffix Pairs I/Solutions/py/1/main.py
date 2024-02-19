class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        # n = len(str1)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        if len(str1) > len(str2):
            return False
        return str2.startswith(str1) and str2.endswith(str1)
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # n = len(words)
        # m = len(words[i])
        # Time Complexity:  O(n * m)
        # Space Complexity: O(1)
        
        counter = 0
        
        for i in range(len(words)):
            word1 = words[i]
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if self.isPrefixAndSuffix(word1, word2):
                    counter += 1
        
        return counter
        