class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # n = len(jewels)
        # m = len(stones)
        # Time Complexity:  O(m)
        # Space Complexity: O(n)

        jewels_set = set(jewels)
        total = 0

        for stone in stones:
            if stone in jewels:
                total += 1

        return total