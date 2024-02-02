class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        tmp = []
        
        for num in arr:
            tmp.append(num)
            if len(arr) == len(tmp):
                break
            if num == 0:
                tmp.append(0)
            if len(arr) == len(tmp):
                break
        
        for i, num in enumerate(tmp):
            arr[i] = num