class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

       n = len(nums)

       for i in range(len(nums)):
           # hide 2 numbers ('a' and 'b') in one number ('x') and use module to get 'b' and division to get 'a' from 'x'
           # x = a + (b % n) * n
           # b = x % n
           # a = x // n
           a = nums[i]
           b = nums[a]
           # if b is greater than n it means it was changed so use module to get the original number
           if b >= n:
                b %= n
           nums[i] = a + (b % n) * n

       for i in range(len(nums)):
            nums[i] //= n

       return nums