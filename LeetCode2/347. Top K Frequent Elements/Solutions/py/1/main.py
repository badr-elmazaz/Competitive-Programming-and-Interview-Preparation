from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # time  -> O(n)
        # space -> O(n)

        nums_frequency = defaultdict(int)
        frequency_nums = defaultdict(set)

        output = []
        max_frequency = 0

        # calculate for each num its frequency in a hashmap

        for num in nums: # time -> O(n)
            current_num_frequency = nums_frequency[num]
            if current_num_frequency in frequency_nums:
                frequency_nums[current_num_frequency].remove(num)
                if len(frequency_nums[current_num_frequency]) == 0:
                    frequency_nums.pop(current_num_frequency)
            nums_frequency[num] += 1
            frequency_nums[current_num_frequency+1].add(num)
            max_frequency = max(max_frequency, current_num_frequency+1)

        for frequency in range(max_frequency, 0, -1): # time -> O(max_frequency)
            for num in frequency_nums[frequency]:
                if k == 0:
                    break
                output.append(num)
                k -= 1
                
        return output





        
        