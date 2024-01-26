class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        
        count_spots = 0
        n = len(arr)
        end = 0

        for i in range(len(arr)):
            current_num = arr[i]

            if current_num == 0:
                count_spots += 2
            else:
                count_spots += 1

            if count_spots == n:
                end = i
                break
            elif count_spots > n:
                end = i - 1
                arr[-1] = arr[i]
                n -= 1
                break

        if not end:
            return

        left = end
        right = n - 1

        while left >= 0:
            current_num = arr[left]
            if current_num == 0:
                arr[right] = 0
                arr[right - 1] = 0
                right -= 2
            else:
                arr[right] = current_num
                right -= 1

            left -= 1