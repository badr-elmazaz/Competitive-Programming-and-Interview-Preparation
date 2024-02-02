class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # n = n
        # m = m
        # Time Complexity:  O(n + m)
        # Space Complexity: O(n + m)
        
        ans = []

        i = 0
        j = 0

        while i < m or j < n:
            num1 = nums1[i] if i < m else float("+inf")
            num2 = nums2[j] if j < n else float("+inf")

            if num1 < num2:
                ans.append(num1)
                i += 1
            else:
                ans.append(num2)
                j += 1

        for i in range(len(nums1)):
            nums1[i] = ans[i]