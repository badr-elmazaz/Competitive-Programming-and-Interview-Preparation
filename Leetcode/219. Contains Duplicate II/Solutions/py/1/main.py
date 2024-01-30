class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        hashtable = {}

        for i, num  in enumerate(nums):
            if num in hashtable and abs(i - hashtable[num]) <= k:
                return True
            hashtable[num] = i

        return False