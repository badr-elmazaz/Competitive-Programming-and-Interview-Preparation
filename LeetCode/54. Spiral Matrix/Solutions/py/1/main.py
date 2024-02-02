class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # time -> O(n*m)
        # space -> O(n+m)

        direction_legend = {
            "U": "R",
            "R": "D",
            "D": "L",
            "L": "U"
        }
        
        current_direction = "R"
        
        i = 0
        j = 0
        
        spiral = [matrix[0][0]]
        
        vertical_boundaries = set()
        horizontal_boundaries = set()
        
        while len(spiral) < len(matrix)*len(matrix[0]):
            if current_direction == "R":
                j += 1
                while j<len(matrix[0]) and j not in vertical_boundaries:
                    spiral.append(matrix[i][j])
                    j += 1
                j -= 1
                
                horizontal_boundaries.add(i)
                current_direction = direction_legend[current_direction]
                
            elif current_direction == "D":
                i += 1
                while i<len(matrix) and i not in horizontal_boundaries:
                    spiral.append(matrix[i][j])
                    i += 1

                i -= 1
                
                vertical_boundaries.add(j)
                current_direction = direction_legend[current_direction]
                
            elif current_direction == "L":
                j -= 1
                while j >=0 and j not in vertical_boundaries:
                    spiral.append(matrix[i][j])
                    j -= 1
                j += 1
                horizontal_boundaries.add(i)
                current_direction = direction_legend[current_direction]
                    
            else:
                i -= 1
                while i >= 0 and i not in horizontal_boundaries:
                    spiral.append(matrix[i][j])
                    i -= 1
                i += 1
                
                vertical_boundaries.add(j)
                current_direction = direction_legend[current_direction]
                
        return spiral
 