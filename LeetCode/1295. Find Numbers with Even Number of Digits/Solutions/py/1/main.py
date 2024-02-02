class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # n = len(nums) : m = len(max(nums))
        # Time Complexity:  O(n * m)
        # Space Complexity: O(m)
        
        counter = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                counter += 1

        return counter