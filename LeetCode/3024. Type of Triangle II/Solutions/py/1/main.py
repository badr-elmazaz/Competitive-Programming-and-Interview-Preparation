class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"

        nums_set = set(nums)

        if len(nums_set) == 3:
            return "scalene"

        if len(nums_set) == 2:
            return "isosceles"

        return "equilateral"