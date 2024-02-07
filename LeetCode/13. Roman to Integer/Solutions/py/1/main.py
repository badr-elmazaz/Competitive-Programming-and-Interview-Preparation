class Solution:
    def romanToInt(self, s: str) -> int:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        legend = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0

        for i in range(len(s) - 1):
            current_char = s[i]
            next_char = s[i + 1]

            adding_num = legend[current_char] * (
                -1 if legend[current_char] < legend[next_char] else 1
            )
            num += adding_num

        return num + legend[s[-1]]
