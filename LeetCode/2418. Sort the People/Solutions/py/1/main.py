class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashtable = {}

        for i, height in enumerate(heights):
            hashtable[height] = i

        heights.sort(reverse=True)

        ans = []

        for height in heights:
            name_idx = hashtable[height]
            name = names[name_idx]
            ans.append(name)

        return ans




