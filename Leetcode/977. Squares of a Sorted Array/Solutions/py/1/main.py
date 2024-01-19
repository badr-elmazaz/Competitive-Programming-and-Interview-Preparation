class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        result = []

        left = 0
        right = len(nums) - 1

        while left <= right:
            left_num = nums[left]
            right_num = nums[right]

            if abs(left_num) <= abs(right_num):
                result.append(right_num ** 2)
                right -= 1

            else:
                result.append(left_num ** 2)
                left += 1

        return reversed(result)
         