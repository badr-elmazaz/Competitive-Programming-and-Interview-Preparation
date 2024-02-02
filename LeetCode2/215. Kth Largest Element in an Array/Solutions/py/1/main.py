from collections import defaultdict

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       # n = len(nums) ; m = max(nums[i])
       # Time Complexity:  O(max(n, m))
       # Space Complexity: O(n)
       
       hashtable_counter = defaultdict(int)

       maximum = nums[0]
       minimum = nums[0]

       for num in nums:
           maximum = max(num, maximum)
           minimum = min(num, minimum)
           hashtable_counter[num] += 1

       for num in range(maximum, minimum - 1, -1):

           if num in hashtable_counter:
               if k <= hashtable_counter[num]:
                   return num
               else:
                   k -= hashtable_counter[num]
                   hashtable_counter.pop(num)