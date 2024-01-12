def isValidSubsequence(array, sequence):
    index_to_check = 0
    for num in array:
        if num == sequence[index_to_check]:
            index_to_check += 1
            if index_to_check == len(sequence):
                break
    return index_to_check == len(sequence)
            
