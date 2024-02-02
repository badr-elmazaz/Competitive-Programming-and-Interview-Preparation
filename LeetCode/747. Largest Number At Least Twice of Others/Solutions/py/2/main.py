from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index_max = 0
        previous_max = nums[index_max]
        max_num = nums[index_max]
        
        for i, num in enumerate(nums):
            if num > max_num:
                index_max = i
                previous_max = max_num
                max_num = num
            
            # (previous_max == max_num) for case nums=[1,0]
            elif num > previous_max or previous_max == max_num:
                previous_max = num
                
    
        return index_max if max_num >= previous_max*2 else -1
        
        
        