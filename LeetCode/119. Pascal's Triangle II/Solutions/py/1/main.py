class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # n = rowIndex
        # Time Complexity:  O(n^2)
        # Space Complexity: O(n)

        if rowIndex == 0:
            return [1]

        elif rowIndex == 1:
            return [1, 1]

        last_row = [1, 1]

        for i in range(rowIndex - 1):
            current_row = [1]

            for j in range(i + 1):
                current_value = last_row[j]
                next_value = last_row[j + 1]
                current_row.append(current_value + next_value)
                
            current_row.append(1)
            last_row = current_row

        return current_row
        