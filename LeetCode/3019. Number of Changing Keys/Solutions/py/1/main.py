class Solution:
    def countKeyChanges(self, s: str) -> int:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        counter = 0
        
        for i in range(1, len(s)):
            current_char = s[i].lower()
            prev_char = s[i - 1].lower()
            
            if current_char != prev_char:
                counter += 1
                
        return counter