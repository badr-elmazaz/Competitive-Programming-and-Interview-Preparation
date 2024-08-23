class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # n = len(word)
        # Time Complexity:  O(n)
        # Space Complexity: O(26)=O(1)

        hashmap = {}
        total = 0

        for i, k in enumerate(keyboard):
            hashmap[k] = i

        prev_position = 0
        for char in word:
            total += abs(prev_position - hashmap[char])
            prev_position = hashmap[char]

        return total