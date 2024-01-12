from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index_max = 0
        max_num = nums[index_max]
        
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                index_max = i
        
        for i, num in enumerate(nums):
            if num*2 > max_num and i != index_max:
                return -1
        return index_max
        
        
        