class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        s = s.strip()

        counter = 0
        for char in reversed(s):
            if char == " ":
                break
            counter += 1

        return counter
        