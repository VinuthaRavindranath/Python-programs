### 13. Find the Maximum and Minimum Number of a Given List of Values
def find_max_min(numbers):
    """
    Find the maximum and minimum numbers in a list.
    
    Parameters:
    numbers (list): The list of numbers.
    
    Returns:
    tuple: (max, min)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    max_num = min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num

# Example usage
print(find_max_min([3, 5, 1, 9, 2]))  # Output: (9, 1)

#or

def maxAndMin(list):
    return max(list),min(list)

list=[3, 5, 1, 9, 2]
max,min=maxAndMin(list)
print(f"max number is {max} and min number is {min}")