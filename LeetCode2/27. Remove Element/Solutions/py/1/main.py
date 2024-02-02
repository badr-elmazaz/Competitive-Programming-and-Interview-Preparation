from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] != val:
                left += 1
            elif nums[right] != val:
                nums[left] = nums[right]
                right -= 1
            else:
                right -= 1

        return left

        

