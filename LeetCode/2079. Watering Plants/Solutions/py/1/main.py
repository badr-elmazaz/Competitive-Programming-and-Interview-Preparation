class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # n  = len(plants)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        total_steps = 0
        current_capacity = capacity

        for i, current_plant in enumerate(plants):
            total_steps += 1

            if current_capacity < current_plant:
                total_steps += 2 * i
                current_capacity = capacity

            current_capacity -= current_plant

        return total_steps