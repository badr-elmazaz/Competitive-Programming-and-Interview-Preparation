class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # n = len(tasks)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(1)

        tasks.sort(reverse = True)
        processorTime.sort()

        ans = tasks[0] + processorTime[0]

        for i in range(4, len(tasks), 4):
            max_task = tasks[i] + (processorTime[i // 4])
            ans = max(ans, max_task)

        return ans