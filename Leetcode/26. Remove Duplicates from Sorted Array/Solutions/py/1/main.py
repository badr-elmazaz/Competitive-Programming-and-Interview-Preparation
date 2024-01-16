from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        count = 0

        for i in range(len(nums)):
            if i == (len(nums) - 1) or nums[i] != nums[i + 1]:
                nums[count] = nums[i]
                count += 1

        return count