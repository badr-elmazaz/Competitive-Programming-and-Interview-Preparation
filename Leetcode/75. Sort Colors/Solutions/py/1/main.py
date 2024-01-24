class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1) 

        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            current_num = nums[i]

            if current_num == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            elif current_num == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right  -= 1
            else:
                i += 1