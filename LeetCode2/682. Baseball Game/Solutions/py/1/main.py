from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation.lstrip("-").isnumeric():
                record.append(int(operation))
            elif operation == "C" and len(record)>0:
                record.pop()
            elif operation == "D" and len(record)>0:
                record.append(record[-1]*2)
            elif len(record)>1:
                record.append(record[-1]+record[-2])

        return sum(record)