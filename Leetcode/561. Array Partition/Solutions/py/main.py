class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(1)

        nums.sort()
        maximum = 0

        for i in range(len(nums)-1, -1, -2):
            maximum += min(nums[i], nums[i - 1])

        return maximum

        