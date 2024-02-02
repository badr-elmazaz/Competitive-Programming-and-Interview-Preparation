class Solution:
    def get_number_of_digits(self, num: int) -> int:
        counter = 0 

        while num != 0:
            num //= 10
            counter += 1

        return counter

    def findNumbers(self, nums: List[int]) -> int:
        # n = len(nums) : m = len(max(nums))
        # Time Complexity:  O(n * log(m))
        # Space Complexity: O(1)
        
        counter = 0

        for num in nums:
            if self.get_number_of_digits(num) & 1 == 0:
                counter += 1

        return counter
        