class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # n = len(s) = len(t)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        hash_map = {}
        total = 0

        for index, (char_s, char_t) in enumerate(zip(s, t)):
            if char_s == char_t:
                continue

            if char_s not in hash_map:
                hash_map[char_s] = index
            else:
                total += abs(index - hash_map[char_s])
                hash_map.pop(char_s)

            if char_t not in hash_map:
                hash_map[char_t] = index
            else:
                total += abs(index - hash_map[char_t])
                hash_map.pop(char_t)

        return total
