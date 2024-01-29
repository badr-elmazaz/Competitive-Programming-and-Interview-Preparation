import bisect 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # Time Complexity: O(log(n))
        # Space Complexity: O(1)
        
        ans = [0] * 2
        
        i = bisect.bisect_left(nums, target)
        count = 0
        while i < len(nums):
            current_num = nums[i]
            if current_num == target:
                count += 1
            elif count != 0 and current_num != target:
                break
            i += 1

        end = (i - 1) if count else -1
        start = (end - count + 1) if count else -1
        ans[0] = start
        ans[1] = end

        return ans