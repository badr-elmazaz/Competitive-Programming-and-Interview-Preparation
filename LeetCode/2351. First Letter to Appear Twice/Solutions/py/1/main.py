class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        seen = set()

        for char in s:
            if char in seen:
                return char
            seen.add(char)
