class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        maximum = -1

        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = maximum
            maximum = max(tmp, maximum)

        return arr