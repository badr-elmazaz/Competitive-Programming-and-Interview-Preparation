class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # n = len(Nums)
        # Time Complexity: O(log(n))
        # Space Complexity: O(1)
        
        start = 0
        end = len(nums) - 1
      
        while start <= end:
            pivot = (start + end) // 2
            current_value = nums[pivot]
            if start == end:
                if current_value < target:
                    return pivot + 1
                else:
                    return pivot
            if current_value == target:
                return pivot
            elif current_value < target:
                start = pivot + 1
            else:
                end = pivot - 1
                
        return pivot