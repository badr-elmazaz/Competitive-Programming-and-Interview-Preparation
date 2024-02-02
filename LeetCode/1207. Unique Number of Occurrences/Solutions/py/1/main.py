from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        hashtable = defaultdict(int)

        for num in arr:
            hashtable[num] += 1

        hashset = set()
        
        for frequency in hashtable.values():
            if frequency in hashset:
                return False
            hashset.add(frequency)
        
        return True
