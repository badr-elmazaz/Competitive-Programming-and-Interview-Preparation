class Solution:
    def is_substring_from_beginning(self, string: str, substring: str) -> bool:
        # n = len(substring)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        for char_string, char_substring in zip(string, substring):
            if char_string != char_substring:
                return False

        return True

    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        # k = k
        # n = len(word)
        # m = n // k
        # Time Complexity:  O(m * n)
        # Space Complexity: O(n)

        min_time = 1
        n = len(word) // k

        while min_time <= n:
            current_substring = word[min_time * k : :]
            if self.is_substring_from_beginning(word, current_substring):
                break

            min_time += 1

        return min_time