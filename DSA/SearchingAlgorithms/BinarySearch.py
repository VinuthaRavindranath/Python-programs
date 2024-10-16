## 2.Binary Search

def binary_search(lst, target):
    """
    Performs a binary search for a target value in a sorted list.

    Parameters:
    lst (list): The sorted list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        if lst[mid] == target:
            return mid  # Target found
        elif lst[mid] < target:
            low = mid + 1  # Search the upper half
        else:
            high = mid - 1  # Search the lower half
    
    return -1  # Target not found

# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 7

result = binary_search(sorted_list, target_value)
if result != -1:
    print(f"Target found at index {result}.")
else:
    print("Target not found.")
