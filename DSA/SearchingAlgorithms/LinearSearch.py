## 1.Linear Search

def linear_search(lst, target):
    """
    Performs a linear search for a target value in a list.

    Parameters:
    lst (list): The list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Example usage:
my_list = [3, 5, 7, 9, 11]
target_value = 77

result = linear_search(my_list, target_value)
if result != -1:
    print(f"Target found at index {result}.")
else:
    print("Target not found.")
