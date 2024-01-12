class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # not meeting the problem's constraints
        # time  -> O(n)
        # space -> O(1)
        # it changes the input array
        
        i = 0
        while i < len(nums):
            if nums[i] == i+1:
                i += 1
            elif nums[i] == nums[nums[i]-1]:
                return nums[i]
            else:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp    