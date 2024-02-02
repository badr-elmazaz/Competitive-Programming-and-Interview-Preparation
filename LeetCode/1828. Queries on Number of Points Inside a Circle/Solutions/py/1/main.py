class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
       # n = len(queries)
       # m = len(points)
       # Time Complexity:  O(n * m)
       # Space Complexity: O(n)

       ans = []

       for query in queries:
           xc, yc, rc = query
           inner_points = 0

           for point in points:
               xp, yp = point
               x_abs = abs(xc-xp)
               y_abs = abs(yc-yp)
               distance_from_center = math.sqrt(x_abs**2 + y_abs**2)

               if distance_from_center <= rc:
                   inner_points += 1
                   
           ans.append(inner_points)

       return ans