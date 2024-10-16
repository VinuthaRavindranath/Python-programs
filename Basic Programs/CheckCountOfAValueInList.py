## 21. To Check How Many Times a Specific Value is Present in the List

def count_occurrences(lst, value):
    """
    Count how many times a specific value is present in the list.
    
    Parameters:
    lst (list): The list to check.
    value: The value to count.
    
    Returns:
    int: The number of occurrences of value.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return lst.count(value)

# Example usage
print(count_occurrences([1, 2, 3, 1, 2, 1], 1))  # Output: 3
