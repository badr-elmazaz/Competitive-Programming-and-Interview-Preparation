from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k