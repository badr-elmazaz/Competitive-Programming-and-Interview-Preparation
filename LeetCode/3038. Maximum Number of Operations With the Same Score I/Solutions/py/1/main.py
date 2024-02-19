class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        prev_score = nums[0] + nums[1]
        count = 1

        for i in range(2, len(nums) - 1, 2):
            current_num = nums[i]
            next_num = nums[i + 1]
            score = current_num + next_num
                
            if score != prev_score:
                break
            
            count += 1
            
        return count