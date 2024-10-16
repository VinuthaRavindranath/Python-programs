### 35. To Find the Missing Number
def find_missing_number(nums):
    """
    Find the missing number in a list containing numbers from 1 to n.
    
    Parameters:
    nums (list): The list of numbers.
    
    Returns:
    int: The missing number.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

# Example usage
print(find_missing_number([1, 2, 4, 5]))  # Output: 3