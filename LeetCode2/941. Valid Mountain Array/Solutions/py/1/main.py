class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        if len(arr)  < 3:
           return False

        maximum_idx = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[maximum_idx]:
                maximum_idx = i

        if maximum_idx == 0 or maximum_idx == len(arr) - 1:
            return False
        
        for i in range(1, maximum_idx + 1):
            if not arr[i] > arr[i - 1]:
                return False

        
        for i in range(maximum_idx + 1, len(arr)):
            if not arr[i - 1] > arr[i]:
                return False

        return True