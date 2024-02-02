class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # n = rowIndex
        # Time Complexity:  O(n^2)
        # Space Complexity: O(n)

        last_row = current_row = [1]

        for i in range(1, rowIndex + 1):
            current_row = [0] * (i + 1) 

            for j in range(i):
                current_row[j] += last_row[j]
                current_row[j + 1] += last_row[j]
                
            last_row = current_row


        return current_row