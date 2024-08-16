class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # n = len(words)
        # m = len(word)
        # Time Complexity:  O(n*m)
        # Space Complexity: O(n)

        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)

        return ans