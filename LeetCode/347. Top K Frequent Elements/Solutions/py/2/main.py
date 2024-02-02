from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # time  -> O(n)
        # space -> O(n)
        
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        bucket = [[] for _ in range(len(nums))]

        for num, count in hashmap.items():
            bucket[count-1].append(num)

        output = []
        
        for i in range(len(nums)-1, -1, -1):
            for num in bucket[i]:
                output.append(num)
                k -= 1
                if k == 0:
                    break
            if k == 0:
                break

        return output

        
        