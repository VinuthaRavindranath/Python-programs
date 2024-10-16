### 8. Reverse a List of Values
def reverse_list(lst):
    """
    Reverse a given list.
    
    Parameters:
    lst (list): The list to reverse.
    
    Returns:
    list: The reversed list.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for the new list.
    """
    return lst[::-1]


# Example usage
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]