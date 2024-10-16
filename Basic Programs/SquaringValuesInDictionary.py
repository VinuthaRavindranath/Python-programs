### 26. Squaring the Values Present in the Dictionaries
def square_values(dictionary):
    """
    Square the values in a dictionary.
    
    Parameters:
    dictionary (dict): The dictionary with numeric values.
    
    Returns:
    dict: A new dictionary with squared values.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return {key: value ** 2 for key, value in dictionary.items()}

# Example usage
print(square_values({'a': 1, 'b': 2}))  # Output: {'a': 1, 'b': 4}