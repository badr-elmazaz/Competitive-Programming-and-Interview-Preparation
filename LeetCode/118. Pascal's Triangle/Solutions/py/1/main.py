from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(numRows-1):
            current_row = [1]
            for j in range(1, i+1):
                last_row = output[-1]
                current_row.append(last_row[j-1]+last_row[j])
            current_row.append(1)
            output.append(current_row)
            
        return output