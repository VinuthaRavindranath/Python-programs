## 32. Check if the Given String Has All Unique Characters

def has_unique_characters(s):
    """
    Check if a string has all unique characters.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if all characters are unique, else False.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(s) == len(set(s))

# Example usage
print(has_unique_characters("hello"))  # Output: False