class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # n = len(aliceSizes)
        # m = len(bobSizes)
        # Time Complexity:  O(n)
        # Space Complexity: O(n + m)

        alice_sizes = aliceSizes
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)

        bob_sizes_set = set(bobSizes)

        diff = sum_alice - sum_bob
        fair_distribution = diff // 2

        for num in alice_sizes:
            target = num - fair_distribution
            if target in bob_sizes_set:
                return [num, target]