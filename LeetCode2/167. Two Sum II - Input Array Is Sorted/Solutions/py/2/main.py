class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n = len(numbers)
        # Time Complexity  -> O(n)
        # Space Complexity -> O(1)
        
        left = 0
        right = len(numbers) - 1
        
        while left <= right:
            sum_num = numbers[left] + numbers[right]
            if sum_num == target:
                return [left + 1, right + 1]
            elif sum_num > target:
                right -= 1
            else:
                left += 1
