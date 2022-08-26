def binary_search(list, item):
    """
    This function takes a sorted array and an item. 
    If the item is in the array, the function returns its position. 
    """
    # high & low check what part of the list to search
    low = 0
    high = len(list) - 1

    # if remaining elements is more than one
    while low <= high:
        # get the middle element as the guess
        mid = (low+high)/2
        guess = list[mid]

        # if guess is equal item
        if guess == item:
            return mid

        # if guess is too high else is too low
        if guess > item:
            # update new high
            high = mid - 1
        else:
            # update new low
            low = mid - 1
    return None


print(binary_search([1, 2, 3, 4, 5, 6], 3)) 
