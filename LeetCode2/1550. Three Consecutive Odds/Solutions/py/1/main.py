class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        odd_counter = 0

        for num in arr:
            if num & 1 != 0:
                odd_counter +=1
            else:
                odd_counter = 0
            if odd_counter == 3:
                break

        return odd_counter == 3