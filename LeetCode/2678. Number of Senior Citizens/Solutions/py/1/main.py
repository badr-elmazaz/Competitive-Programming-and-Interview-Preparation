class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # n = len(details)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        counter = 0

        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                counter += 1

        return counter