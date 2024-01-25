class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # n = len(travel)
        # m = len(max(garbage[i]))
        # Time Complexity:  O(n * m)
        # Space Complexity: O(1)
        
        glass_time = 0
        paper_time = 0
        metal_time = 0

        glass_total = 0
        paper_total = 0
        metal_total = 0
    
        travel.insert(0, 0)
        for t, g in zip(reversed(travel), reversed(garbage)):
            glass_quantity = 0
            paper_quantity = 0
            metal_quantity = 0

            for char in g:
                if char == "G": glass_quantity += 1
                elif char == "P": paper_quantity += 1
                else: metal_quantity += 1

            if glass_time or glass_quantity and not glass_time:
                glass_time += t
            if paper_time or paper_quantity and not paper_time:
                paper_time += t
            if metal_time or metal_quantity and not metal_time:
                metal_time += t
            
            glass_total += glass_quantity
            paper_total += paper_quantity
            metal_total += metal_quantity


        return glass_total + paper_total + metal_total + glass_time + paper_time + metal_time