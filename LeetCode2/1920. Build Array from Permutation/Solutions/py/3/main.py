class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
       # n = len(nums)
       # Time Complexity:  O(n)
       # Space Complexity: O(1)

       n = len(nums)

       for i in range(len(nums)):
           a = nums[i]
           b = nums[a]
           nums[i] += (b % n) * n


       for i in range(len(nums)):
            nums[i] //= n

       return nums