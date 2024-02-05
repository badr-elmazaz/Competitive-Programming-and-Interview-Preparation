class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        current_sum = 0

        counter = 0

        for num in nums:
            current_sum += num
            if current_sum == 0:
                counter += 1

        return counter
