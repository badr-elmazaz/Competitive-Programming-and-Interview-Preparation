from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        frequencies = Counter(nums)
        
        bucket = [0] * len(nums)
        
        for num, frequency in frequencies.items():
            bucket[frequency - 1] += frequency
            
            
        for num in reversed(bucket):
            if num != 0:
                return num
            