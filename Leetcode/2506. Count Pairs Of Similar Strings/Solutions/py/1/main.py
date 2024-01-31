class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # n = len(words)
        # Time Complexity:  O(n^2)
        # Space Complexity: O(n)

        pairs = 0
        for i, string in enumerate(words):
            words[i] = set(string)

        for i in range(len(words)):
            string1 = words[i]
            for j in range(i + 1, len(words)):
                string2 = words[j]
                if string1 == string2:
                    pairs += 1

        return pairs