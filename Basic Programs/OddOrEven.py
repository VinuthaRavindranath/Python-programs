
### 1. Odd or Even
def is_odd_or_even(num):
    """
    Check if a number is odd or even.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    str: "Even" if the number is even, "Odd" if it is odd.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return "Even" if num % 2 == 0 else "Odd"

#Example usage
print(is_odd_or_even(10))  # Output: Even