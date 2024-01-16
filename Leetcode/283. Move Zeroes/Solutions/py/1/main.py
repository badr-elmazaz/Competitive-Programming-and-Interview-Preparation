class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        left = 0
        right = 0

        while left <= right and right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                # swap
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] != 0:
                left += 1
            if nums[right] == 0 or right < left:
                right += 1
        
            
