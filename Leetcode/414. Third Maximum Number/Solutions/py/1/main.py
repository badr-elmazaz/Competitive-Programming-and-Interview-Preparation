class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        first_max, second_max, third_max = nums[0], float("-inf"), float("-inf")

        for i in range(1, len(nums)):
            current_num = nums[i]
            
            if current_num == first_max or current_num == second_max or current_num == third_max:
                continue
            
            if current_num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = current_num

            elif current_num > second_max:
                third_max = second_max
                second_max = current_num

            elif current_num > third_max:
                third_max = current_num

        
        return third_max if third_max != float("-inf") else first_max