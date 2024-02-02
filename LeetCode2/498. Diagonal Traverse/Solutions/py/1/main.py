from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(i, j)
                hashmap[i+j].append(mat[i][j])
            
        output = []
        left = True
        for i in range(len(mat)+len(mat[0])):
            current_list = hashmap.get(i)
            if current_list:
                if left:
                    for j in range(len(current_list)-1, -1, -1):
                        output.append(current_list[j])
                else:
                    for num in current_list:
                        output.append(num)
                left = not left

                
        return output
            