class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # n = len(word)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        word = list(word)

        ch_idx = 0
        for i, char in enumerate(word):
            if char == ch:
                ch_idx = i
                break

        for i in range((ch_idx + 1) // 2):
            word[i], word[ch_idx - i] = word[ch_idx - i], word[i]

        return "".join(word)
