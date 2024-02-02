class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        idx = len(s) - 1
        current_char = s[idx]

        # skip all the last spaces
        while current_char == " " and idx >= 0:
            idx -= 1
            current_char = s[idx]

        counter = 0
        
        # count the word
        while current_char != " " and idx >= 0:
            counter += 1
            idx -= 1
            current_char = s[idx]

        return counter