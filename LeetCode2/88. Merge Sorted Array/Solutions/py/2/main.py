class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # n = n
        # m = m
        # Time Complexity:  O(n + m)
        # Space Complexity: O(1)

        i = m - 1
        j = n - 1

        for k in range(n + m - 1, -1, -1):
            num1 = nums1[i] if i >= 0 else float("-inf")
            num2 = nums2[j] if j >= 0 else float("-inf")

            if num1 < num2:
                nums1[k] = num2
                j -= 1
            else:
                nums1[k] = num1
                i -= 1