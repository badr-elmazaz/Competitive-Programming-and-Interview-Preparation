class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # n = len(heights)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(n)

        ans = 0
        expecteds = sorted(heights)

        for height, expected in zip(heights, expecteds):
            if height != expected:
                ans += 1


        return ans