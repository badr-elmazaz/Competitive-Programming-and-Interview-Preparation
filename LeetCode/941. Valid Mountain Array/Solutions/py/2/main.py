class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        i = 1

        while i < len(arr) and arr[i] > arr[i - 1]:
            i += 1

        if i == 1 or i == len(arr) or arr[i] == arr[i - 1]:
            return False
        
        while i < len(arr) and arr[i] < arr[i - 1]:
            i += 1

        return i == len(arr)