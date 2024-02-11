class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        if not nums:
            return []
        if len(nums) == 1:
            return list(map(str, nums))

        start = nums[0]

        output = []

        for i in range(1, len(nums)):
            current_num = nums[i]
            prev_num = nums[i - 1]
            if current_num - prev_num != 1:
                if start == prev_num:
                    output.append(str(start))
                else:
                    output.append(f"{start}->{prev_num}")
                start = current_num

        if start == current_num:
            output.append(str(start))
        else:
            output.append(f"{start}->{current_num}")
        return output
