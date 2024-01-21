from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
      # n = len(nums)
      # Time complexity:  O(n)
      # Space complexity: O(k) 
        
      hashtable = defaultdict(int)
      
      left = 0
      right = k - 1
      running_sum = 0
      maximum = 0
      
      #craete the window
      for i in range(k):
        current_val = nums[i]
        hashtable[current_val] += 1
        running_sum += current_val

      if len(hashtable) == k:
          maximum = running_sum 
          
                 
      # slide the window
      while right < len(nums) - 1:
        last_left_val = nums[left]
        hashtable[last_left_val] -= 1
        if hashtable[last_left_val] == 0:
          hashtable.pop(last_left_val)
        running_sum -= last_left_val
        left += 1
        right += 1
        new_right_val = nums[right]
        running_sum += new_right_val
        hashtable[new_right_val] += 1
    
        if len(hashtable) == k:
            maximum = max(maximum, running_sum)
          
          
      return maximum
        