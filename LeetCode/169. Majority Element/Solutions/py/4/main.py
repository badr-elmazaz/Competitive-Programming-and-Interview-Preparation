class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        count = 0

        for num in nums:
            if count == 0:
                ans = num

            if num != ans:
                count -= 1
            else:
                count += 1

        return ans
