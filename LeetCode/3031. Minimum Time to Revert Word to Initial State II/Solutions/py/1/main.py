class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        # k = k
        # n = len(word)
        # m = n // k
        # Time Complexity:  O(m * n)
        # Space Complexity: O(n)

        min_time = 1
        n = len(word) // k

        while min_time <= n:
            if word[: -min_time * k] == word[min_time * k : :]:
                break
            min_time += 1

        return min_time