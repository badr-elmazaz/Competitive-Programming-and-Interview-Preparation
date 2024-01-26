class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # n = len(nums1)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        ans = []

        i = 0
        j = 0
        n2 = len(nums2)
        n1 = abs(n2 - len(nums1))

        while i < n1 or j < n2:
            num1 = nums1[i] if i < n1 else float("+inf")
            num2 = nums2[j] if j < n2 else float("+inf")

            if num1 < num2:
                ans.append(num1)
                i += 1
            else:
                ans.append(num2)
                j += 1

        for i in range(len(nums1)):
            nums1[i] = ans[i]