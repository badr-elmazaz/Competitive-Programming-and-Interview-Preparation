class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n = len(nums1)
        # m = len(nums2)
        # Time Complexity:  O(n + m)
        # Space Complexity: O(n + m)
        
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        if len(nums1_set) > len(nums2_set):
            big = nums1_set
            small = nums2_set
        else:
            big = nums2_set
            small = nums1_set

        output = []

        for num in small:
            if num in big:
                output.append(num)

        return output
        