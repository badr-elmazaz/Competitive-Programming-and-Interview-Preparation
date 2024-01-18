class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      # n = len(prices)
      # Time Complexity:  O(n)
      # Space Complexity: O(1)
      
      counter = 0
      
      for i in range(len(prices) - 1):
        current_price = prices[i]
        if current_price < prices[i + 1]:
          counter += prices[i + 1] - current_price
      
      
      return counter