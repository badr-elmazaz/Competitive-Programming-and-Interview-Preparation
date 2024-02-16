class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n = len(nums1)
        # m = len(nums2)
        # Time Complexity:  O(n + m)
        # Space Complexity: O(n + m)

        return list(set(nums1).intersection(set(nums2)))
        