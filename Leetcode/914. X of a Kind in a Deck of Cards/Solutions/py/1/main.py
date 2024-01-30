class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashtable_counter = Counter(deck)

        gcd = math.gcd(*hashtable_counter.values())

        return gcd != 1