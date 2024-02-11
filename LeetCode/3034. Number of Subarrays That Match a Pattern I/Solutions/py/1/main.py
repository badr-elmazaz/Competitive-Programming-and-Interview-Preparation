class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # n = len(nums)
        # m = len(pattern)
        # Time Complexity:  O(n * m)
        # Space Complexity: O(1)
        
        ans = 0
        m = len(pattern)

        for i in range(len(nums) - m):
            for k, p in enumerate(pattern):
                current_num = nums[i + k]
                next_num = nums[i + k + 1]
                if (
                    (p == 1 and current_num >= next_num)
                    or (p == 0 and current_num != next_num)
                    or (p == -1 and current_num <= next_num)
                ):
                    break
            else:
                ans += 1

        return ans
