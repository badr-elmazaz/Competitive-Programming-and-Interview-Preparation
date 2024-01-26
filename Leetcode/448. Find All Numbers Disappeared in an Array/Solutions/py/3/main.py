class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)


        missing_nums = []

        for i in range(len(nums)):
            current_num = abs(nums[i])
            nums[current_num - 1] = abs(nums[current_num - 1]) * -1


        for i in range(len(nums)):
            if nums[i] > 0:
                missing_nums.append(i + 1)

        return missing_nums