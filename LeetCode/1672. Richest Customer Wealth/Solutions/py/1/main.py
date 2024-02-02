class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
       # n = len(accounts)
       # m = len(accounts[0])
       # Time Complexity:  O(n * m)
       # Space Complexity: O(1)
       
       maximum = float("-inf")

       for i in range(len(accounts)):
           total = 0
           for j in range(len(accounts[0])):
               total += accounts[i][j]
            
           maximum = max(total, maximum)

       return maximum
