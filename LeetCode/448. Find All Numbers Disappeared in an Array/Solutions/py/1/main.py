class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        hashset = set(nums)

        missing_nums = []

        for num in range(1, len(nums) + 1):
            if num not in hashset: missing_nums.append(num)


        return missing_nums