class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        return " ".join(s.split(" ")[:k])