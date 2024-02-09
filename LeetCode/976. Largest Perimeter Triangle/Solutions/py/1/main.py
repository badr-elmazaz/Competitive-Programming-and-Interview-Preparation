class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(1)

        nums.sort(reverse = True)

        i = 0

        max_perimeter = 0

        while i + 2 < len(nums):
            current_num = nums[i]
            next_num = nums[i + 1]
            next_next_num = nums[i + 2]

            if current_num < next_num + next_next_num:
                max_perimeter = current_num + next_num + next_next_num
                break
            i += 1

        return max_perimeter