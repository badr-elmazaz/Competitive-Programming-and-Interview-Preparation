class Solution:
    def scoreOfString(self, s: str) -> int:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        score = 0
        for i in range(len(s) - 1):
            curr_char_ord = ord(s[i])
            next_char_ord = ord(s[i + 1])
            score += abs(curr_char_ord - next_char_ord)

        return score