class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(1)

        nums.sort()
        
        limit = len(nums) // 2

        for num in nums:
            if nums[limit] == num:
                return num
