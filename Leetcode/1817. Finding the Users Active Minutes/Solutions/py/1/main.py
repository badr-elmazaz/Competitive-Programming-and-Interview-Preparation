class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
       # n = len(logs)
       # Time Complexity:  O(n)
       # Space Complexity: O(n)
       
       answer = [0] * k

       hashtable = defaultdict(set)

       for log in logs:
           user, minute = log

           hashtable[user].add(minute)

       for user, minutes in hashtable.items():
            answer[len(minutes) - 1] += 1

       return answer 