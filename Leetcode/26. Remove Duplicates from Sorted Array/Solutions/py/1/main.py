from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                nums[count] = nums[i]
                count+=1

        #for i in range(count, len(nums)):
        #    nums[i] = "_"

        return count