class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        ans = []
        hashtable = defaultdict(set)

        for person, group_size in enumerate(groupSizes):
            hashtable[group_size].add(person)


        for group_size, people in hashtable.items():
            group = []
            for person in people:
                group.append(person)
                if len(group) == group_size:
                    ans.append(group)
                    group = []


        return ans


        
            

        