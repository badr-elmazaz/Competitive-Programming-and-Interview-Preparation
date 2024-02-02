class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n = len(numbers)
        # Time Complexity  -> O(n * log(n))
        # Space Complexity -> O(1)
        
        def search_idx_number(number: int, index_to_avoid: int) -> int: # O(log(n))
            # binary search
            start = 0
            end = len(numbers) - 1
            while start <= end:
                mid = (start + end) // 2
                # if there are duplicates
                if mid == index_to_avoid:
                    mid += 1
                if number == numbers[mid]:
                    return mid
                elif number > numbers[mid]:
                    start = mid + 1
                else:
                    end = mid - 1 

            return -1
        
        for i in range(len(numbers)): # O(n)
           num_to_search = target - numbers[i]
           idx_num_to_search = search_idx_number(num_to_search, i)
           if idx_num_to_search > -1:
               return [i + 1, idx_num_to_search + 1]

