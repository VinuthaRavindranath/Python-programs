### 5. Reverse a String
def reverse_string(s):
    """
    Reverse a given string.
    
    Parameters:
    s (str): The string to reverse.
    
    Returns:
    str: The reversed string.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for the new string.
    """
    return s[::-1]

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
