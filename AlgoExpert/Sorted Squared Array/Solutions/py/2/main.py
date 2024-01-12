def sortedSquaredArray(array):
    negatives = []
    output = []

    i = 0
    while i < len(array):
        current_num = array[i]
        if current_num < 0:
            negatives.append(current_num**2)
            i += 1
        elif negatives and current_num**2 > negatives[-1]:
            output.append(negatives.pop())
        else:
            output.append(current_num**2)
            i += 1

    if negatives:
        output += reversed(negatives) # O(n)


    return output
