class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        shift = ord("A") - 1
        total = 0
        for i, char in enumerate(reversed(columnTitle)):
            total += (ord(char) - shift) * pow(26, i)
        return total