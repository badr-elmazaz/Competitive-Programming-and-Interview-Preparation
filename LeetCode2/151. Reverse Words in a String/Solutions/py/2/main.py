class Solution:
    def reverseWords(self, s: str) -> str:
        # n = len(s)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # using builtin functions is faster even if it is the same time and space complexity

        reverse_words = []
        for word in reversed(s.split()):
            if word:
                reverse_words.append(word)

        return " ".join(reverse_words) 