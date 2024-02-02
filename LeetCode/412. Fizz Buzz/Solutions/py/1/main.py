class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # n = n
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        output = []
        for i in range(1, n + 1):

            output.append("")
            if i % 3 == 0:
                output[-1] += "Fizz"
            if i % 5 == 0:
                output[-1] += "Buzz"
            if not output[-1]:
                output[-1] = str(i)

        return output
                
            
        