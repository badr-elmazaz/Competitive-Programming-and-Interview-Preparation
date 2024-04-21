class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Time Complexity:  O(1)
        # Space Complexity: O(1)
        
        char, num = list(coordinates)
        return ord(char) + int(num) & 1 != 0