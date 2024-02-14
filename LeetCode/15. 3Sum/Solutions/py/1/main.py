class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # Time Complexity:  O(n^2)
        # Space Complexity: O(1)
        
        nums.sort()

        output = []

        target = 0

        for i in range(len(nums) - 2):
            x = nums[i]
            if i != 0 and nums[i - 1] == x:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                total = left_num + right_num + x
                if target == total:
                    output.append([left_num, right_num, x])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
                

        return output
