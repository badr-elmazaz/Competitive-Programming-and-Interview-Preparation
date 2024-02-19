class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # n = len(list1)
        # m = len(list2)
        # Time Complexity:  O(n + m)
        # Space Complexity: O(n + m)

        hashmap = defaultdict(int)

        for i, s in enumerate(list1):
            hashmap[s] = i

        hashmap2 = defaultdict(int)

        for i, s in enumerate(list2):
            if s in hashmap:
                hashmap2[s] = i + hashmap[s]

        minimum = min(hashmap2.values())

        output = []

        for k, v in hashmap2.items():
            if v == minimum:
                output.append(k)

        return output
