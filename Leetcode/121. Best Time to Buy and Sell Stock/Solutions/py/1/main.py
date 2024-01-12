from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0
        for num in prices:
            if num-minimum > maximum:
                maximum = num-minimum
            if num < minimum:
                minimum = num


        return maximum