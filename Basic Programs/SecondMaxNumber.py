### 14. Find the Second Maximum Number in a Given List of Values
def second_max(numbers):
    """
    Find the second maximum number in a list.
    
    Parameters:
    numbers (list): The list of numbers.
    
    Returns:
    int: The second maximum number.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")
    
    first, second = float('-inf'), float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second

# Example usage
print(second_max([3, 5, 1, 9, 2]))  # Output: 5