from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        
        for i, num in enumerate(nums):
            if total - num - left_sum == left_sum:
                return i
            else:
                left_sum += num
            
        return -1