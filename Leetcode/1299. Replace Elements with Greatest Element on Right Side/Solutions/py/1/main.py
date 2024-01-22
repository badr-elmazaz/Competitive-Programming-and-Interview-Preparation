class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        maximum = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            tmp = arr[i]
            arr[i] = maximum
            maximum = max(tmp, maximum)

        arr[-1] = -1
        return arr