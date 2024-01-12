class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # time  -> O(nlogn)
        # space -> O(n)
        
        nums1.sort()
        nums2.sort(reverse=True)
        return sum(a*b for a, b in zip(nums1, nums2))