def sortedSquaredArray(array):
    squared = [0] * len(array)

    left = 0
    right = len(array) - 1
    squared_pointer = len(squared) - 1
    while left <= right:
        if abs(array[left]) > abs(array[right]):
            squared[squared_pointer] = array[left]**2
            left += 1
        else:
            squared[squared_pointer] = array[right]**2
            right -= 1
        squared_pointer -= 1

    return squared
        
