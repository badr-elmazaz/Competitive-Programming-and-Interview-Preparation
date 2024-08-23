class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        r_count = 0
        l_count = 0

        ans = 0

        for char in s:
            if char == "R":
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                ans += 1
                r_count = 0
                l_count = 0

        return ans