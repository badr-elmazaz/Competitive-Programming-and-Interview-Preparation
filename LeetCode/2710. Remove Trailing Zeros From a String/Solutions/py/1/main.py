class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        for i, char in enumerate(reversed(num)):
            if char != "0":
                break
        
        return num[:len(num) - i]

                