class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
            
        
       counter = 0
       maximum = 0

       for num in nums:
           if num == 1:
               counter +=  1
           else:
                maximum = max(maximum, counter)
                counter = 0
        
       return max(maximum, counter)