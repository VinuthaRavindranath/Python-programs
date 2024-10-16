## 37. Rotate an array to the right by k steps.

def rotate_array(arr, k):
    """
    Rotate an array to the right by k steps.
    
    Parameters:
    arr (list): The array to rotate.
    k (int): The number of steps to rotate.
    
    Returns:
    list: The rotated array.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for the new array.
    """
    n = len(arr)
    k %= n  # Handle k greater than n
    return arr[-k:] + arr[:-k]

# Example usage
print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
    