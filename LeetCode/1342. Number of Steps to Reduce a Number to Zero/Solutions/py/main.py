class Solution:
    def numberOfSteps(self, num: int) -> int:
        # n = num
        # Time Complexity:  O(log(n))
        # Space Complexity: O(1)

        count = 0

        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1

        return count      