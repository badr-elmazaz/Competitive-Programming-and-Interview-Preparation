from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right_sum = [0]
        
        for i in range(1, len(nums)):
            left_sum.append(left_sum[i-1]+nums[i-1])
            
        for i in range(len(nums)-2, -1, -1):
            right_sum.append(right_sum[len(nums)-2-i]+nums[i+1])
            
        for i in range(len(nums)):
            if left_sum[i] == right_sum[len(nums)-1-i]:
                return i
            
        return -1