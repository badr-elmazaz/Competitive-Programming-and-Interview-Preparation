class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # n = len(moves)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)
        
        counter = Counter(moves)
        return counter.get("U", 0) == counter.get("D", 0) and counter.get("R", 0) == counter.get("L", 0)
