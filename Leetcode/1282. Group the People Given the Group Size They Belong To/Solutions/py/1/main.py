class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # n = len(groupSizes)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        ans = []
        hashtable = defaultdict(list)

        for person, group_size in enumerate(groupSizes):
            hashtable[group_size].append(person)

            if len(hashtable[group_size]) == group_size:
                ans.append(hashtable[group_size])
                hashtable.pop(group_size)

        return ans