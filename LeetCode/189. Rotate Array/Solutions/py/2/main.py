class Solution(object):

    def reverse(self, from_idx: int, to_idx: int, array: list[object]) -> None:
        # n = ((to_idx - from_idx) // 2)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        # to_idx is excluse
        start = from_idx
        end = (from_idx + to_idx) // 2
        next_idx = to_idx - 1

        for current_idx in range(start, end):
            array[current_idx], array[next_idx] = array[next_idx], array[current_idx]
            next_idx -= 1



    def rotate(self, nums, k):
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        start, end = 0, len(nums)
        self.reverse(start, end, nums)

        start, end = 0, k % len(nums)
        self.reverse(start, end, nums)

        start, end = k % len(nums), len(nums)
        self.reverse(start, end, nums)

        return nums

    