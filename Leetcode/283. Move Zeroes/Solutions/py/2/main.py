class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        left = 0

        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
