class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        left_even = 0
        right_odd = len(nums) - 1

        while left_even < right_odd:

            if nums[left_even] & 1 != 0 and nums[right_odd] & 1 == 0:
                nums[left_even], nums[right_odd] = nums[right_odd], nums[left_even]
   
            if nums[left_even] & 1 == 0:
                left_even += 1

            if nums[right_odd] & 1 != 0:
                right_odd -= 1 

        return nums