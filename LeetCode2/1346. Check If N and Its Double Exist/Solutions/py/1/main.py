class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        hashtable = {}

        for i, num in enumerate(arr):
            hashtable[num] = i

        for i, num in enumerate(arr):
            double = num * 2
            if hashtable.get(double, i) != i:
                return True
        
        return False
        