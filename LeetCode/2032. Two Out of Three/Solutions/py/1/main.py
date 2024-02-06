class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        # n = len(nums1)
        # m = len(nums2)
        # o = len(nums3)
        # Time Complexity:  O(n + m + o)
        # Space Complexity: O(n + m + o)

        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)

        ans = set()

        for num in nums1_set:
            if num in nums2_set or num in nums3_set:
                ans.add(num)

        for num in nums2_set:
            if num in nums1_set or num in nums3_set:
                ans.add(num)

        for num in nums3_set:
            if num in nums2_set or num in nums1_set:
                ans.add(num)

        return list(ans)
