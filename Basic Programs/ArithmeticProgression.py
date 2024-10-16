## 29. Arithmetic Progression (AP)
def arithmetic_progression(a, d, n):
    """
    Generate the first n terms of an arithmetic progression.
    
    Parameters:
    a (int): The first term.
    d (int): The common difference.
    n (int): The number of terms.
    
    Returns:
    list: The first n terms of the AP.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return [a + i * d for i in range(n)]

# Example usage
print(arithmetic_progression(1, 2, 5))  # Output: [1, 3, 5, 7, 9]