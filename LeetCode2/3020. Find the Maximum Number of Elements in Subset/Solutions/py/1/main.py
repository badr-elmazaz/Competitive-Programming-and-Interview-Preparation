class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        hashtable_counter = Counter(nums)

        # handle ones, check if num of ones is even or odd
        total_ones = hashtable_counter[1] 

        if total_ones and total_ones & 1 == 0:
            total_ones -= 1

        if total_ones:
            hashtable_counter.pop(1)
        
        max_subset = max(total_ones, 1)
        
        for current_num in hashtable_counter.keys():

            if hashtable_counter[current_num] == 1:
                continue
            
            subset = 0 
            
            next_num = current_num ** 2 
            
            while True:
                if hashtable_counter[current_num] > 1 and hashtable_counter[next_num]:
                    current_num, next_num = next_num, next_num ** 2
                    subset += 2

                elif hashtable_counter[current_num] == 1 or not hashtable_counter[next_num]:
                    subset += 1
                    max_subset = max(subset, max_subset)
                    break
    
              
        return max_subset