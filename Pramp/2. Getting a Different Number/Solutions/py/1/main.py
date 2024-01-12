def get_different_number(arr):
    # time  -> O(n)
    # space -> O(n)
    
    seen = {num for num in arr}
  
    for i in range(len(arr) + 1):
        if i not in seen:
            return i