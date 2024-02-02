class Solution:
    def minimumPushes(self, word: str) -> int:
        # n = len(word)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        current_cost = 1
        ans = 1

        for counter in range(1, len(word)):
            if counter % 8 == 0:
                current_cost += 1
            ans += current_cost
            
            
        return ans