class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
       # n = len(nums)
       # Time Complexity:  O(n)
       # Space Complexity: O(n)

       ans = []
       
       for i in range(len(nums)):
           ans.append(nums[nums[i]])

       return ans