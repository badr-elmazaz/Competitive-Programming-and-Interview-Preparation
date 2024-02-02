class Solution(object):
    def rotate(self, nums, k):
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)


        hashset = {}


        for i, num in enumerate(nums):
            hashset[i] = num

        for i in range(len(nums)):
            new_idx = (i + k) % len(nums)
            nums[new_idx] = hashset[i]

        return nums
