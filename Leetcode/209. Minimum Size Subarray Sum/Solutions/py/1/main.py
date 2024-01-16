class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        current_sum = 0
        minimum = float("inf")
        left = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= target:
                minimum = min(minimum, i - left + 1)
                current_sum -= nums[left]
                left += 1

        return minimum if minimum != float("inf") else 0
