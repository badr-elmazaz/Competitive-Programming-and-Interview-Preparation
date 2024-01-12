from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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

        

