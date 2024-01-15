class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        xor = 0 # neutral element
        for num in nums:
            xor ^= num

        return xor
        
        