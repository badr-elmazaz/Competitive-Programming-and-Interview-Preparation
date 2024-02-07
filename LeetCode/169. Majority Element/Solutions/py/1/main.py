class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        num_counter = Counter(nums)

        for num, frequency in num_counter.items():
            if frequency > len(nums) // 2:
                return num
