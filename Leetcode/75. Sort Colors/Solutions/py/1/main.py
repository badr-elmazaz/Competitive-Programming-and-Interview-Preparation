class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        zero_count = 0
        one_count = 0


        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
        
        for i in range(len(nums)):
            if zero_count == 0:
                if one_count == 0:
                    nums[i] = 2
                
                else:
                    nums[i] = 1
                    one_count -= 1

            else:
                nums[i] = 0
                zero_count -= 1
        