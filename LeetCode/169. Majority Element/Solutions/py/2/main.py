class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(1)

        nums.sort()

        count = 1
        limit = len(nums) // 2
        current_num = nums[0]

        for i in range(1, len(nums)):
            current_num = nums[i]
            prev_num = nums[i - 1]

            if current_num == prev_num:
                count += 1
            else:
                count = 1

            if count > limit:
                return current_num

        return current_num
