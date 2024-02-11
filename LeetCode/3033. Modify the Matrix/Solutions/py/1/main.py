class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # n = len(matrix)
        # m = len(matrix[0])
        # Time Complexity: O(n * m)
        # Space Complexity: O(n)

        for col in range(len(matrix[0])):
            rows_with_target_num = []
            maximum = float("-inf")

            for row in range(len(matrix)):
                current_num = matrix[row][col]
                maximum = max(maximum, current_num)
                if current_num == -1:
                    rows_with_target_num.append(row)

                for row in rows_with_target_num:
                    matrix[row][col] = maximum

        return matrix
