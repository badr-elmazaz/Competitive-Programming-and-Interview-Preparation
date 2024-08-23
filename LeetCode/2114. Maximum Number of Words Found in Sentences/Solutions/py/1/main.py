class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # n = len(sentences)
        # m = len(sentences[i])
        # Time Complexity:  O(n * m)
        # Space Complexity: O(1)

        maximum = 0
        for sentence in sentences:
            num_words = 1
            for char in sentence:
                if char == " ":
                    num_words += 1
            maximum = max(maximum, num_words)

        return maximum


